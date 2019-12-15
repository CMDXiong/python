# encoding: utf-8

# TCP: socket.SOCK_STREAM
# UDP: socket.SOCK_DGRAM

import socket
HOST = '127.0.0.1'
PORT = 65432
# 第一参数是地址族
    # ip4:socket.AF_INET
    # ip6:socket.AF_INET6
# 第二个参数：socket类型
    # TCP: socket.SOCK_STREAM
    # UDP: socket.SOCK_DGRAM
my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 关联 socket 到指定的网络接口（IP 地址）和端口号，
# 第一个参数主机名称、IP 地址、空字符串，只有主机上的进程可以连接到服务器
    # 空：服务器将接受本机所有可用的IPv4地址
my_socket.bind((HOST, PORT))
# 返回连接状态和客户端地址

# backlog参数：允许连接的请求数量
my_socket.listen()

# accept() 方法阻塞并等待传入连接
# 返回一个新的socket对象conn，你将用这个 socket 对象和客户端进行通信，和监听一个 socket 不同的是后者只用来授受新的连接请求
# 以及返回一个由主机、端口号组成的 IPv4/v6 连接的元组addr
conn, addr = my_socket.accept()
with conn:
    print('Connected by', addr)
    while True:
        data = conn.recv(1024)
        if not data:
            break
        conn.sendall(data)


my_socket.close()


# with socket.socket(HOST, PORT) as my_socket:
#     pass
