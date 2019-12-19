# encoding: utf-8
import socket
import struct
import json
import os
import threading


class MYTCPServer:
    address_family = socket.AF_INET
    socket_type = socket.SOCK_STREAM
    allow_reuse_address = False
    max_packet_size = 8192
    coding = 'utf-8'
    request_queue_size = 5
    server_dir = os.path.join(os.path.dirname(__file__), 'file_upload')

    def __init__(self, server_address, bind_and_activate=True):
        self.server_address = server_address
        self.socket = socket.socket(self.address_family, self.socket_type)
        if bind_and_activate:
            try:
                self.bind()
                self.activate()
            except:
                self.close()
                raise

    def bind(self):
        if self.allow_reuse_address:
            self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind(self.server_address)
        self.server_address = self.socket.getsockname()

    def activate(self):
        self.socket.listen(self.request_queue_size)

    def close(self):
        self.socket.close()

    def get_request(self):
        return self.socket.accept()

    def close_request(self, request):
        request.close()

    def run(self):
        while True:
            conn, client_addr = self.get_request()
            print('from client', client_addr)
            socket_handle = MySocketHandle(conn, client_addr)

            # 用线程来处理每一个连接
            client_thread = threading.Thread(target=socket_handle.handle_sock, args=())
            client_thread.start()
        self.close()


class MySocketHandle(object):
    max_packet_size = 8192
    coding = 'utf-8'
    header_len = 4  # 报头头部固定长度
    server_dir = os.path.join(os.path.dirname(__file__), 'file_upload')

    def __init__(self, socket, client_addr):
        self.socket = socket
        self.client_addr = client_addr

    def make_header_and_send(self, header_dict):
        """ 制作报头并发送，需要一个报头的dict存储报头信息"""
        print("发送数据的报头", header_dict)
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

    def handle_sock(self):
        print('from client', self.client_addr)
        while True:
            try:
                head_dict = self.recv_header()
                # 客户端断开后：
                if not head_dict: break
                print("接收的命令报头：", head_dict)
                cmd = head_dict['cmd']
                if hasattr(self, cmd):
                    func = getattr(self, cmd)
                    func(head_dict)
            except Exception:
                break
        self.close()

    def put(self, head_dict):
        """上传文件的操作"""
        file_path = os.path.normpath(os.path.join(self.server_dir, head_dict['filename']))
        filesize = head_dict['filesize']
        recv_size = 0
        print('----->', file_path)
        with open(file_path, 'wb') as f:
            while recv_size < filesize:
                recv_data = self.socket.recv(self.max_packet_size)
                f.write(recv_data)
                recv_size += len(recv_data)
                print('recvsize:{} filesize {}'.format(recv_size, filesize))

    def get(self, head_dict):
        """下载文件的操作"""
        filename = head_dict['filename']
        file_path = os.path.normpath(os.path.join(self.server_dir, filename))
        if not os.path.isfile(file_path):
            print('file:{} is not exists'.format(file_path))
            return
        else:
            filesize = os.path.getsize(file_path)

        header_dict = {
            'filename': filename,
            'md5': 'xxxxx',
            'filesize': filesize
        }
        # 发送下载的头部
        self.make_header_and_send(header_dict)

        # 发送真实的文件数据
        send_size = 0
        with open(file_path, 'rb') as f:
            for line in f:
                self.socket.send(line)
                send_size += len(line)
                print("总数据：{}------已发送：{}".format(filesize, send_size))
            else:
                print('download successful')

    def close(self):
        self.socket.close()
        print('Connection from %s:%s closed.' % self.client_addr)


def main():
    tcpserver = MYTCPServer(('127.0.0.1', 8080), bind_and_activate=True)
    tcpserver.run()


if __name__ == "__main__":
    main()