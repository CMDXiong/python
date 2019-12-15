def gen_func():
    try:
        yield "www.baidu.com"
    except Exception as e:
        pass
    yield 2
    yield 3
    return "panxiong"


if __name__ == "__main__":
    gen = gen_func()
    print(next(gen))
    # 在yield "www.baidu.com"抛异常
    gen.throw(Exception, "download error")
    print(next(gen))
    # 在yield 2抛异常
    gen.throw(Exception, "download error")