# coding=utf-8
import threading
# Event对象wait的方法只有在内部信号为真的时候才会很快的执行并完成返回。当Event对象的内部信号标志位假时，
# 则wait方法一直等待到其为真时才返回。也就是说必须set新号标志位真


def do(event):
    print('start')
    event.wait()
    print('execute')


event_obj = threading.Event()
for i in range(10):
    t = threading.Thread(target=do, args=(event_obj,))
    t.start()

event_obj.clear()
inp = input('输入内容:')
if inp == 'true':
    event_obj.set()