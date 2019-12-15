# encoding: utf-8

import socket

HOST = '127.0.0.1'  # 服务器的主机名或者 IP 地址
PORT = 65432        # 服务器使用的端口
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s_client:
    s_client.connect((HOST, PORT))
    s_client.sendall(b'Hello, world')
    # 1024 是缓冲区数据大小限制最大值参数 bufsize，并不是说 recv() 方法只返回 1024 个字节的内容
    # send() 方法也是这个原理，它返回发送内容的字节数，结果可能小于传入的发送内容，你得处理这处情况，
    # 按需多次调用 send() 方法来发送完整的数据
    # 和 send() 方法不一样的是，sendall() 方法会一直发送字节，只到所有的数据传输完成或者中途出现错误。
    # 成功的话会返回 None 引用
    data = s_client.recv(1024)

print(data)
print('Received', repr(data))

