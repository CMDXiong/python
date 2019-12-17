# coding=utf-8
# import os
# #fork只能用于linux/unix中
# pid = os.fork()
# print("bobby")
# if pid == 0:
#   print('子进程 {} ，父进程是： {}.' .format(os.getpid(), os.getppid()))
# else:
#   print('我是父进程：{}.'.format(pid))

import multiprocessing

#多进程编程
import time
def get_html(n):
    time.sleep(n)
    print("sub_progress success")
    return n


# 进程类
class MyProcessing(multiprocessing.Process):
    def run(self):
        pass


if __name__ == "__main__":
    # progress = multiprocessing.Process(target=get_html, args=(2,))
    # print(progress.pid)
    # progress.start()
    # print(progress.pid)
    # progress.join()
    # print("main progress end")

    #使用进程池
    pool = multiprocessing.Pool(multiprocessing.cpu_count())
    # result = pool.apply_async(get_html, args=(3,))
    #
    # #等待所有任务完成
    # pool.close()是让进程池不再接受新的任务
    # pool.close()
    # pool.join()
    #
    # print(result.get())

    # imap
    # 完成的顺序和添加的顺序一样
    # for result in pool.imap(get_html, [1,5,3]):
    #     print("{} sleep success".format(result))

    # 完成的顺序和添加的顺序不一样
    for result in pool.imap_unordered(get_html, [1,5,3]):
        print("{} sleep success".format(result))

