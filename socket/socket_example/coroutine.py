# 协程是为了解决回调编写难的问题
# 1.回调模式编码复杂度高
# 2.同步编程的并发性不高
# 3.多线程编程需要线程间同步，lock

# 1.采用同步的方式去编写异步的代码
# 2.使用单线程去切换任务
#       1.线程是由操作系统切换的，单线程切换意味着我们需要程序员自己去调度任务
#       2.不在需要锁，并发性高，如果单线程内切换函数，性能远高于线程切换，并发性更高


# 我们需要一个可以暂停的函数，并且可以在适当的时候恢复该函数的继续执行，
# 因此出现了协程 ->有多个入口的函数，可以暂停的函数（可以向暂停的地方传入值）

# 生成器可以实现暂停

def gen_func():
    # 1.可以产出值，2.可以接收值（调用方传递进来的值）
    html = yield "http://www.baidu.com"
    print(html)
    yield 2
    yield 3
    return "panxiong"

# 1.throw, close

# 1.生成器不只可以产出值，还可以接收值


if __name__ == "__main__":
    gen = gen_func()
    # 在调用send发送非None值之前，我们必须启动一次生成器，方式有两种
    #1.gen.send(None), 2.next(gen)
    # 1.启动生成器的方式有两种，next(), send()
    url = next(gen)
    html = "panxiong"
    gen.send(html)
    # print(next(gen))
    # print(next(gen))
    # print(next(gen))
    # print(next(gen))