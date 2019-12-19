import socket
import os
import subprocess
import struct

# 此种解决方案的不足
# 1.报头信息少
# 2.数据长度有限制


def main():
    ssh_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 使用端口可以重用
    # ssh_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    ssh_server.bind(("127.0.0.1", 8083))
    ssh_server.listen(5)
    while True:
        conn, addr = ssh_server.accept()
        while True:
            try:
                # 1.收命令
                cmd = conn.recv(1024)
                if not cmd: break
                print("客户端数据", cmd)

                # 2.执行命令，拿到结果
                # 执行系统命令，os模块
                # 0: 命令执行成功，非0: 命令执行不成功
                # res = os.system(cmd)
                # 默认打到终端，
                obj = subprocess.Popen(cmd.decode("utf-8"), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                # 如果是linux,默认的utf-8，如果是windows，则是GBK
                stdout = obj.stdout.read()  # 返回的是bytes类型
                stderr = obj.stderr.read()  # 返回的是bytes类型

                # 3.把命令的结果返回给客户端
                # 3.1 制作固定长度的报头
                # 复用stuct模块来解决
                # struct.pack() 第一个参数：格式，第二个参数, i是4个字节，l是8个字节
                total_size = len(stdout) +len(stderr)
                header = struct.pack('i', total_size)

                # 3.2 把报头(固定长度)发送给客户端
                conn.send(header)

                # 3.3 再发送真实的数据
                # conn.send(stdout+stderr)  # +是一个可以优化的点
                conn.send(stdout)
                conn.send(stderr)
            except ConnectionResetError:
                break
        conn.close()


if __name__ == "__main__":
    main()
