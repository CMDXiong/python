# encoding: utf-8
# socket 客户端编写示例
import socket
import struct
import json


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
            obj = client.recv(4)
            head_size = struct.unpack('i', obj)[0]
            # 2.2再收报头
            header_bytes = client.recv(head_size)
            # 2.3 从报头中解析出真实数据的描述信息
            header_json = header_bytes.decode('utf-8')
            header_dic = json.loads(header_json)
            total_size = header_dic['total_size']

            # 2.4接受真实的数据
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
