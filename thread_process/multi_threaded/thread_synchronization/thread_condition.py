# coding=utf-8
# 条件变量， 用于复杂的线程间同步
# 启动顺序很重要
# 在调用with con之后才能调用wait或者notify方法
# condition有两层锁，一把底层锁会在线程调用了wait方法的时候释放,
# 上面的锁会在每次调用wait的时候分配一把并放入到cond的等待队列中，等到notify方法的唤醒


import threading
import time

con = threading.Condition()
num = 0
# 生产者
class Producer(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        # 锁定线程
        global num
        con.acquire()
        while True:
            print("开始添加！！！")
            num += 1
            print("火锅里面鱼丸个数：%s" % str(num))
            time.sleep(1)
            if num >= 5:
                print("火锅里面里面鱼丸数量已经到达5个，无法添加了！")
                # 唤醒等待的线程
                con.notify()  # 唤醒小伙伴开吃啦
                # 等待通知
                con.wait()
        # 释放锁
        con.release()


# 消费者
class Consumers(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        # 用with的方式来打开Condition
        with con:
            global num
            while True:
                print("开始吃啦！！！")
                num -= 1
                print("火锅里面剩余鱼丸数量：%s" % str(num))
                time.sleep(2)
                if num <= 0:
                    print("锅底没货了，赶紧加鱼丸吧！")
                    con.notify()  # 唤醒其它线程
                    # 等待通知
                    con.wait()


if __name__ == "__main__":
    p = Producer()
    c = Consumers()
    p.start()
    c.start()