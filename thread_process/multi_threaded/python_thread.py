# coding=utf-8
# GIL global interpreter lock (cpython)
# python中一个线程对应于c语言中的一个线程
# GIL使得同一时刻只有一个线程在一个cpu上执行字节码，无法将多个线程映射到多个cpu上执行
# GIL会根据执行的字节码行数以及时间片释放GIL，GIL在遇到io的操作进修主动释放

#对于io操作来说，多线程和多进程性能差别不大

#1.通过Thread类实例化
# import time
# import threading
# def get_detail_html(url):
#     print("get detail html started")
#     time.sleep(2)
#     print("get detail html end")
#
#
# def get_detail_url(url):
#     print("get detail url started")
#     time.sleep(4)
#     print("get detail url end")
#
#
# if  __name__ == "__main__":
#     thread1 = threading.Thread(target=get_detail_html, args=("", ))
#     thread2 = threading.Thread(target=get_detail_url, args=("", ))
#     # setDaemon设置成守护线程，当主线程关闭后，子线程也会关闭
#     # thread1.setDaemon(True)
#     # thread2.setDaemon(True)
#     start_time = time.time()
#     thread1.start()
#     thread2.start()
#
#     # join方法阻塞，等待两个线程的完成，再执行主线程
#     thread1.join()
#     thread2.join()
#
#     #当主线程退出的时候， 子线程kill掉
#     print ("last time: {}".format(time.time()-start_time))


# 2.通过继承Thread来实现多线程
import time
import threading
class GetDetailHtml(threading.Thread):
    def __init__(self, name):
        # 线程的名字
        super().__init__(name=name)

    # 重载run方法，run方法里面写逻辑
    def run(self):
        print("get detail html started")
        time.sleep(2)
        print("get detail html end")


class GetDetailUrl(threading.Thread):
    def __init__(self, name):
        super().__init__(name=name)

    def run(self):
        print("get detail url started")
        time.sleep(4)
        print("get detail url end")


if __name__ == "__main__":
    thread1 = GetDetailHtml("get_detail_html")
    thread2 = GetDetailUrl("get_detail_url")
    start_time = time.time()
    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    #当主线程退出的时候， 子线程kill掉
    print("last time: {}".format(time.time()-start_time))