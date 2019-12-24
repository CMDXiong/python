import socket
import os
from multiprocessing import Process
from pprint import pprint


class StaticWebSever(object):
    STATUS_CODE = {200: "OK", 404: "未找到"}

    def __init__(self, port=80, maxfd=5):
        self.listen_sock = socket.socket()
        self.listen_sock.bind(('', port))
        self.listen_sock.listen(maxfd)
        print("监听socket:{}对象成功".format(port))

        self.request_dict = {}    # 保存请求HTTP头的字段信息
        self.filename = ""        # 保存实际的文件路径

        self.new_sock = socket.socket()

    def run_server(self):
        while True:
            self.new_sock, addr = self.listen_sock.accept()
            print("有一个新链接：{}".format(addr))
            pl = Process(target=self.process_handler)
            pl.start()
            self.new_sock.close()  # 有新的进程维护了新链接，服务器进程没有必要保留

    # 循环接收请求头信息
    def _recv_request_header(self):
        buf = self.new_sock.recv(1024)
        while buf.find(b'\r\n\r\n') == -1:
            buf += self.new_sock.recv(1024)
        return buf.decode('utf-8')

    def _parse_request(self, buf):
        datas = buf.splitlines()
        head = datas[0]
        self.request_dict['method'] = head.split(" ")[0].strip()
        self.request_dict['name'] = head.split(" ")[1].strip()
        for data in datas[1:]:
            item = data.split(":")
            if len(item) == 2:
                k = item[0].strip()
                self.request_dict[k] = item[1].strip()

    def process_handler(self):
        # 接收浏览器发来的信息
        buf = self._recv_request_header()
        self._parse_request(buf)
        pprint(self.request_dict)
        self.new_sock.close()

    def send_response(self, status):
        response_header = 'HTTP/1.1 {} {}\r\n'.format(status, self.STATUS_CODE[status])


def main_process():
    server = StaticWebSever()
    server.run_server()


if __name__ == "__main__":
    main_process()




