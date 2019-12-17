# encoding: utf-8
# socket客户端以类的方式写
import socket

# 消息必须要么具有固定长度，要么可以界定，要么指定了长度（比较好的做法）
MSGLEN = 4096


class MySocket:
    """demonstration class only
      - coded for clarity, not efficiency
    """

    def __init__(self, sock=None):
        if sock is None:
            self.sock = socket.socket(
                            socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock

    def connect(self, host, port):
        self.sock.connect((host, port))

    def mysend(self, msg):
        totalsent = 0
        while totalsent < MSGLEN:
            sent = self.sock.send(msg[totalsent:])
            if sent == 0:
                break
                # raise RuntimeError("socket connection broken")
            totalsent = totalsent + sent

    def myreceive(self):
        data = self.sock.recv(1024).decode("utf8")
        return data

        # chunks = []
        # bytes_recd = 0
        # while bytes_recd < MSGLEN:
        #     # 当 recv 方法返回 0 字节时，就表示另一端已经关闭（或者它所在的进程关闭）了连接
        #     chunk = self.sock.recv(min(MSGLEN - bytes_recd, 2048))
        #     if chunk == b'':
        #         raise RuntimeError("socket connection broken")
        #     chunks.append(chunk)
        #     bytes_recd = bytes_recd + len(chunk)
        # return b''.join(chunks)

    def close(self):
        self.sock.close()

def main():

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 8000))
    clint_sock = MySocket(client)
    clint_sock.mysend("hello server".encode("utf8"))
    print(clint_sock.myreceive())
    # clint_sock.close()

    # client.send("hello server".encode("utf8"))
    # data = client.recv(1024)
    # print(data.decode("utf8"))
    # client.close()


if __name__ == "__main__":
    main()