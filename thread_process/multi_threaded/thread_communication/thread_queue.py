# coding=utf-8
# 通过queue的方式进行线程间同步
from queue import Queue
import time
import threading
lock = threading.Lock()

num = 0


def get_detail_html(queue):
    #爬取文章详情页
    while True:
        global num
        lock.acquire()
        num += 1
        if num == 20:
            queue.task_done()
            break
        lock.release()
        url = queue.get()                    # 这是一个阻塞的方法，如果queue是空，会阻塞在这里
        print(url)
        time.sleep(2)


def get_detail_url(queue):
    # 爬取文章列表页
    while True:
        print("get detail url started")
        time.sleep(4)
        for i in range(20):
            queue.put("http://projectsedu.com/{id}".format(id=i))
        print("get detail url end")


if __name__ == "__main__":
    detail_url_queue = Queue(maxsize=1000)   # Queue是线程安全的
    thread_detail_url = threading.Thread(target=get_detail_url, args=(detail_url_queue,))
    thread_detail_url.start()
    for i in range(10):
        html_thread = threading.Thread(target=get_detail_html, args=(detail_url_queue,))
        html_thread.start()
    start_time = time.time()

    # detail_url_queue.task_done() # 这条语句需要放在合适的地方
    detail_url_queue.join()

    print("last time: {}".format(time.time()-start_time))

#      Queue.qsize()：返回queue的大小。
#
#    Queue.empty():判断队列是否为空，通常不太靠谱。
#
#    Queue.full():判断是否满了。
#
# 　　 Queue.put(item, block=True, timeout=None): 往队列里放数据。
#  　 Queue.put_nowait(item):往队列里存放元素，不等待
# 　　 Queue.get(item, block=True, timeout=None): 从队列里取数据。
#  　 Queue.get_nowait(item):从队列里取元素，不等待
# 　　 Queue.task_done()：表示队列中某个元素是否的使用情况，使用结束会发送信息。
# 　　 Queue.join()：一直阻塞直到队列中的所有元素都执行完毕。

# Queue.task_done() 在完成一项工作之后，Queue.task_done()函数向任务已经完成的队列发送一个信号
# Queue.join() 实际上意味着等到队列为空，再执行别的操作
# 可以理解为，每task_done一次 就从队列里删掉一个元素，这样在最后join的时候根据队列长度是否为零来判断队列是否结束，从而执行主线程。


