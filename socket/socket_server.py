# encoding: utf-8
import socket
import threading


def recv(sock):
    """接受所有的数据, 数据是字节流"""
    # 1024指最大的接受数据量，但不一定每次都接受1024的数量量
    data = sock.recv(1024).decode("utf8")
    return data

    # data = b""
    # while True:
    #     d = sock.recv(1024)    # 这是一个阻塞函数，当没有数据接收时，recv方法会阻塞
    #     if d:
    #         data += d
    #     else:
    #         break
    # return data.decode("utf8")


def send(sock, data):
    """发送数据给客户端, data为字符串"""
    # socket.send(string[, flags]) 　发送TCP数据，返回发送的字节大小。
    # 这个字节长度可能少于实际要发送的数据的长度。
    # 换句话说，这个函数执行一次，并不一定能发送完给定的数据，可能需要重复多次才能发送完成。
    len = 0
    while True:
        len = sock.send(data[len:].encode("utf8"))
        if not len:
            break

    # 或者用sendall发送完整的TCP数据,如下
    # sock.sendall(data.encode("utf8"))


def handle_sock(sock, addr):
    # 获取从客户端发送的数据
    data = recv(sock)
    # 数据类型解码成utf8
    print(data)
    send(sock, "hello client")


def main():
    # 创建一个socket
    # 第一参数是地址族
    #     ip4: socket.AF_INET
    #     ip6: socket.AF_INET6
    # 第二个参数：socket类型
    #     TCP: socket.SOCK_STREAM
    #     UDP: socket.SOCK_DGRAM
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 关联 socket 到指定的网络接口（IP 地址）和端口号，
    # 第一个参数主机名称、IP 地址、空字符串，只有主机上的进程可以连接到服务器
    # 空：服务器将接受本机所有可用的IPv4地址
    server.bind(('0.0.0.0', 8000))

    # backlog参数：允许连接的请求数量
    server.listen(5)

    while True:
        # accept() 方法阻塞并等待传入连接
        # 返回一个新的socket对象conn，你将用这个 conn 对象和客户端进行通信，
        # 和监听一个 socket（即server） 不同的是后者只用来授受新的连接请求
        # 以及返回一个由主机、端口号组成的 IPv4/v6 连接的元组addr
        sock, addr = server.accept()

        # 用线程去处理新接收的连接（用户）
        client_thread = threading.Thread(target=handle_sock, args=(sock, addr))
        client_thread.start()


if __name__ == "__main__":
    main()



