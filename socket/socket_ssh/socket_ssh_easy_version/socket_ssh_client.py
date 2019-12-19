# encoding: utf-8
# socket 客户端编写示例
import socket
import struct

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 8083))
    while True:
        try:
            # 1.发命令
            cmd = input(">>: ").strip()
            client.send(cmd.encode("utf8"))

            # 2.拿命令的结果，并打印
            # 2.1先收报头（数据的长度）
            header = client.recv(4)

            # 2.2从报头中解析出对真实数据的描述信息（数据的长度）
            total_size = struct.unpack('i',  header)[0]

            # 2.3接受真实的数据
            recv_size = 0  # 已经接受到的数据大小
            recv_data = b''  # 已经接受的数据
            while recv_size < total_size:
                res = client.recv(1024)    # 1024是一个坑
                recv_data += res
                recv_size += len(res)
            # print(data.decode("utf-8"))   # 服务端运行在linux上
            print(recv_data.decode("GBK"))  # 服务端运行在windows上
        except Exception:
            break
    client.close()


if __name__ == "__main__":
    main()
