# encoding: utf-8

import socket
import struct
import json
import os


class MYTCPClient:
    address_family = socket.AF_INET        # 地址族
    socket_type = socket.SOCK_STREAM       # socket类型
    allow_reuse_address = False            # 是否允许地址端口重用
    max_packet_size = 8192                 # 每次接收包的最大大小
    coding = 'utf-8'
    request_queue_size = 5                 # 监听的最在数量
    header_len = 4                         # 报头头部固定长度

    def __init__(self, server_address, connect=True):
        self.server_address = server_address
        self.socket = socket.socket(self.address_family, self.socket_type)
        if connect:
            try:
                self.connect()
            except:
                self.close()
                raise

    def connect(self):
        self.socket.connect(self.server_address)

    def close(self):
        self.socket.close()

    def make_header_and_send(self, header_dict):
        """ 制作报头并发送，需要一个报头的dict存储报头信息"""
        print(header_dict)
        head_json = json.dumps(header_dict)
        head_json_bytes = bytes(head_json, encoding=self.coding)
        head_stuct = struct.pack('i', len(head_json_bytes))
        self.socket.send(head_stuct)
        self.socket.send(head_json_bytes)

    def recv_header(self):
        """接收头部信息"""
        header_struct = self.socket.recv(self.header_len)
        head_len = struct.unpack('i', header_struct)[0]
        head_json = self.socket.recv(head_len).decode('utf-8')
        head_dict = json.loads(head_json)
        return head_dict

    def recv_body(self, head_dict):
        """接收下载的真实的数据"""
        filesize = head_dict['filesize']
        filename = head_dict['filename']

        with open(filename, 'wb') as f:
            recv_size = 0
            while recv_size < filesize:
                line = self.socket.recv(self.max_packet_size)
                f.write(line)
                recv_size += len(line)

    def run(self):
        while True:
            try:
                inp = input(">>: ").strip()  # 命令的形式"get a.txt.txt" 或者"put a.txt.txt"
                if not inp:
                    continue
                inp_list = inp.split()
                cmd = inp_list[0]
                if hasattr(self, cmd):
                    func = getattr(self, cmd)
                    func(inp_list)
            except Exception:
                # 服务端断开
                break
        self.socket.close()

    def put(self, args):
        """上传文件数据的操作"""
        cmd = args[0]
        filename = args[1]
        if not os.path.isfile(filename):
            print('file:{} is not exists'.format(filename))
            return
        else:
            filesize = os.path.getsize(filename)

        # 1.制作上传的报头信息
        header_dict = {
            'cmd': cmd,
            'filename': os.path.basename(filename),
            'md5': 'xxxxx',
            'filesize': filesize
        }
        self.make_header_and_send(header_dict)

        # 2.上传真实的数据
        send_size = 0
        with open(filename, 'rb') as f:
            for line in f:
                self.socket.send(line)
                send_size += len(line)
                print(send_size)
            else:
                print('upload successful')

    def get(self, args):
        """下载文件的操作"""
        # 制作报头dict
        header_dict = {
            'cmd': args[0],
            'filename': args[1],
        }
        # 1.发送下载的命令与文件名
        self.make_header_and_send(header_dict)

        # 2.接收头部, 获取报头信息
        head_dict = self.recv_header()
        print(head_dict)

        # 3.接收真实的数据
        self.recv_body(head_dict)


def main():
    client = MYTCPClient(('127.0.0.1', 8080), connect=True)
    client.run()


if __name__ == "__main__":
    main()