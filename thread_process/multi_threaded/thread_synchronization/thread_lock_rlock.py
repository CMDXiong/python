# coding=utf-8
from threading import Lock, RLock
# Lock
# RLock: 可重入的锁
# 他们的功能，大部分是相同的，很多情况下可以通用，但有细微的区别: 在同一线程内，对RLock进行多次acquire()操作，程序不会阻塞
total = 0
lock = Lock()
def add():
    global lock
    global total
    for i in range(1000000):
        lock.acquire()
        total += 1
        lock.release()


def desc():
    global lock
    global total
    for i in range(1000000):
        lock.acquire()
        total -= 1
        lock.release()


#
rlock = RLock()
def f():
    with rlock:
        g()
        h()


def g():
    with rlock:
        h()
        do_something1()


def h():
    with rlock:
        do_something2()


def do_something1():
    print('do_something1')


def do_something2():
    print('do_something2')


if __name__ == "__main__":
    import threading
    thread1 = threading.Thread(target=add)
    thread2 = threading.Thread(target=desc)
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    print(total)

    # rlock
    # 每个thread都运行f()，f()获取锁后，运行g()，但g()中也需要获取同一个锁。如果用Lock，这里多次获取锁，就发生了死锁。
    # 但我们代码中使用了RLock。在同一线程内，对RLock进行多次acquire()操作，程序不会堵塞
    threading.Thread(target=f).start()
    threading.Thread(target=f).start()
    threading.Thread(target=f).start()


#1. 用锁会影响性能
#2. 锁会引起死锁
#死锁的情况 A（a，b）
"""
A(a、b)
acquire (a)
acquire (b)

B(a、b)
acquire (a)
acquire (b)
"""
