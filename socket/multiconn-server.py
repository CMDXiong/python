# encoding: utf-8

import selectors
import socket

HOST = '127.0.0.1'
PORT = 65432

sel = selectors.DefaultSelector()

lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
lsock.bind((HOST,PORT))
lsock.listen()
print('listening on', (HOST,PORT))

#  配置 socket 为非阻塞模式，这个 socket 的调用将不在是阻塞的。
#  当它和 sel.select() 一起使用的时候（下面会提到），我们就可以等待 socket 就绪事件，
#  然后执行读写操作sel.register() 使用 sel.select() 为你感兴趣的事件注册 socket 监控，
#  对于监听 socket，我们希望使用 selectors.EVENT_READ 读取到事件
lsock.setblocking(False)

# 如果是非阻塞的，调用connect会立马返回，但三次握手还没有完成
lsock.connect((HOST,PORT))

import types
def accept_wrapper(sock):
    conn, addr = sock.accept()
    print('accepted connection from', addr)
    conn.setblocking(False)
    data = types.SimpleNamespace(addr=addr, inb=b'', outb=b'')
    events = selectors.EVENT_READ | selectors.EVENT_WRITE
    sel.register(conn, events, data=data)


def service_connection(key, mask):
    sock = key.fileobj
    data = kkey.data
