def gen_func():
    try:
        yield 1
    except GeneratorExit:
        # 如果此处是pass,什么都不处理，且生成器后面还有yield语句，当使用了close时，close是会抛异常的
        # 如果此处是pass,什么都不处理，且生成器后面没有yield语句，当使用了close时，close是不会抛异常的
        # pass

        # 但是如果此处是raise StopIteration,生成器后面不管有没有yield,调用close时，都不会抛异常
        # 尽量不要自己处理GeneratorExit的异常
        # GeneratorExit是继承自BaseException
        raise StopIteration
    yield 2
    yield 3
    return "panxiong"


if __name__ == "__main__":
    gen = gen_func()
    print(next(gen))
    gen.close()
    next(gen)