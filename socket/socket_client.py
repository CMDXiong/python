# encoding: utf-8
# socket 客户端编写示例
import socket


def recv(sock):
    data = b""
    while True:
        # 这是一个阻塞函数，当没有数据接收时，recv方法会阻塞，d是没有返回的，所以不能用这种while True的方式来接收所有数据
        d = sock.recv(1024)
        if d:
            data += d
        else:
            break
    return data.decode("utf8")


def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 8000))
    client.send("hello server".encode("utf8"))
    data = client.recv(1024)
    print(data.decode("utf8"))
    client.close()


if __name__ == "__main__":
    main()
