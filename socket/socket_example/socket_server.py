# encoding: utf-8
import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 8000))
server.listen()


def handle_sock(sock, addr):
    while True:
        # 数据如果大于1k,该怎么办
        # 一次获取1k的数据
        # 获取从客户端发送的数据
        data = sock.recv(1024)
        print(data.decode("utf8"))
        sock.send("hello world".encode("utf8"))


while True:
    sock, addr = server.accept()
    # 用线程去处理新接收的连接（用户）
    client_thread = threading.Thread(target=handle_sock, args=(sock, addr))
    client_thread.start()

