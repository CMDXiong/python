# 包含各种特定系统实现的模块化事件循环

# 传输和协议抽象

# 对TCP、UDP、SSL、子进程、延时调用以及其他的具体支持

# 模仿futures模块但适用于事件循环使用的Future类

# 基于yield from的协议和任务，可以让你用顺序的方式编写并发代码

# 必须使用一个将产生阻塞IO的调用时，有接口可以把这个事件转移到线程池

# 模仿threading模块中的同步原语，可以用在单线程内的协程之间

# 事件循环 + 回调（驱动生成器） + epoll(I/O多路复用)
# asyncio是python用于解决异步io编程的一整套解决方案
# 基于asyncio的框架tornado, gevent, twisted（scrapy, django channels）
# tornado（实现web服务器）， django+flask(uwsgi, gunicorn + nginx)
# tornado可以直接部署（nginx + tornado）


# 使用asyncio
# import asyncio
# import time
# async def get_html(url):
#     print("start get url")
#     # time.sleep()是一个同步阻塞的接口，不能使用在协程中，不会出错，但会是阻塞
#     # time.sleep(2)
#     # 立即返回，在下一次调度时，会判断时间有没有到，到了后，才会执行下面的语句
#     await asyncio.sleep(2)
#     print("end get url")
#
#
# if __name__ == "__main__":
#     start_time = time.time()
#     # 执行一个任务
#     # loop = asyncio.get_event_loop()  # 事件循环，完成select操作
#     # # 这是一个阻塞的方法,可以简单的理解成一个join方法
#     # loop.run_until_complete(get_html("www.baidu.com"))
#
#     # 执行多个任务
#     loop = asyncio.get_event_loop()
#     tasks = [get_html("www.baidu.com") for i in range(10)]
#     loop.run_until_complete(asyncio.wait(tasks))
#     print(time.time() - start_time)


# 获取协程的返回值
import asyncio
import time
async def get_html(url):
    print("start get url")
    await asyncio.sleep(2)
    return "panxiong"


if __name__ == "__main__":
    # start_time = time.time()
    # loop = asyncio.get_event_loop()
    # get_future = asyncio.ensure_future(get_html("www.baidu.com"))
    # loop.run_until_complete(get_future)
    # print(get_future.result())

    start_time = time.time()
    loop = asyncio.get_event_loop()
    # task是future类的一个子类
    task = loop.create_task(get_html("www.baidu.com"))
    loop.run_until_complete(task)
    print(task.result())
