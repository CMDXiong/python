# -*- encoding: utf-8 -*-
# 用生成器实现一个可迭代对象

# 实际案例
# 实现一个可迭代对象的类, 它能迭代出给定范围内所有素数:
# pn = PrimeNumbers(1,30)
# for k in pn:
#     print(k)
# 输出结果:
# 2,3,5,7,11,13,17,19,23,29

# 解决方案
# 将该类的__iter__方法实现成生成函数, 每次yield返回一个素数.
# 在iterable_iterator.py中实现的迭代器需要手工维护self.index, 现在可实现自动维护
# 使用生成器来实现, 生成器对象是一个可迭代对象, 也是一个迭代器对象
from collections import Iterable
class PrimeNumbers(Iterable):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __iter__(self):
        for k in range(self.a, self.b+1):
            if self.is_prime(k):
                yield k

    def is_prime(self, k):
        return False if k < 2 else all(map(lambda x: k % x, range(2, k)))


if __name__ == "__main__":
    pn = PrimeNumbers(1, 30)
    for n in pn:
        print(n)
    print('-'*20)
    for n in pn:
        print(n)


