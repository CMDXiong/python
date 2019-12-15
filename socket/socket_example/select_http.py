# encoding: utf-8
# 1.epoll并不代表一定比select好
# 在并发高的情况下，连接活跃不是很高，epoll比select好
# 并发性不高，同时连接很活跃，select比epoll好
# 连接活跃：建立一次连接后，不会不再管了，或者明确会断掉，如游戏就是连接活跃

# 通过非阻塞io实现http请求
# 回调+事件循环+select(poll/epoll)
# 并发性高
# 使用单线程

import socket
from urllib.parse import urlparse
from selectors import DefaultSelector, EVENT_WRITE, EVENT_READ
# 1.select库与selectors的区别, selectors是在select基础上包装的一个包，这个包使用的更加方便
# 2.windows下使用select，但是linux下使用的是epoll，如果使用selectors，则不用我们关心使用select还是epoll，
# selectors会根据平台来选择


# 使用select完成http请求
selector = DefaultSelector()
urls = ["http://www.baidu.com"]
stop = False


class Fetcher(object):
    def connected(self, key):
        selector.unregister(key.fd)
        self.client.send("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(self.path, self.host).encode("utf8"))
        selector.register(self.client.fileno(), EVENT_READ, self.readable)

    def readable(self, key):
        d = self.client.recv(1024)
        if d:
            self.data += d
        else:
            selector.unregister(key.fd)

            data = self.data.decode("utf-8")
            html_data = data.split("\r\n\r\n")[1]
            print(html_data)
            self.client.close()

            urls.remove(self.spider_url)
            if not urls:
                global stop
                stop = True

    def get_url(self, url):
        self.spider_url = url

        url = urlparse(url)
        self.host = url.netloc
        self.path = url.path
        self.data = b""
        if self.path == "":
            self.path = "/"

        # 建立连接
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.setblocking(False)

        try:
            self.client.connect((self.host, 80))   # 阻塞不会消耗cpu
        except BlockingIOError as e:
            pass

        # 注册
        # 第一个参数是文件描述符，第二个参数是注册的带伤，第三个参数是回调函数
        selector.register(self.client.fileno(), EVENT_WRITE, self.connected)


def loop():
    # 事件循环，不停的请求socket的状态并调用对应的回调函数
    # 1.select本身是不支持register模式，
    # 2.socket状态变化以后的回调是由程序员完成的
    while not stop:
        # key = ['fileobj', 'fd', 'events', 'data'] ： socket对象, 文件描述符，事件，回调函数
        ready = selector.select()
        for key, mask in ready:
            call_back = key.data
            call_back(key)


if __name__ == "__main__":
    fetcher = Fetcher()
    fetcher.get_url("http://www.baidu.com")
    loop()

