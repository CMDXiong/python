# -*- encoding: utf-8 -*-
# 实现对一个可迭代器对象实现切片操作

# 切片的实质是重载了__getitem__方法
# 解决方案
# 使用itertools.islice, 它能返回一个迭代对象切片的生成器


def my_islice(iterable, start, end, step=1):
    tmp = 0
    for  i, x in enumerate(iterable):
        if i >= end:
            return
        if i >= start:
            if tmp == 0:
                tmp = step
                yield x
            tmp -= 1


print(list(my_islice(range(100, 150), 10, 20, 3)))
from itertools import islice
print(list(islice(range(100, 150), 10, 20, 3)))
