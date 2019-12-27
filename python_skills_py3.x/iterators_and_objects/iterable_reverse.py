# -*- encoding: utf-8 -*-
# 实现反向迭代对象

# 解决方案:
# 实现反向迭代协议的__reversed__方法, 它返回一个反向迭代器

from decimal import Decimal


class FloatRange:
    def __init__(self, a, b, step):
        self.a = Decimal(str(a))
        self.b = Decimal(str(b))
        self.step = Decimal(str(step))

    def __iter__(self):
        t = self.a
        while t <= self.b:
            yield float(t)
            t += self.step

    def __reversed__(self):
        t = self.b
        while t >= self.a:
            yield float(t)
            t -= self.step


if __name__ == "__main__":
    fr = FloatRange(3.0, 4.0, 0.2)
    for x in fr:
        print(x)
    print('-'*20)

    for x in reversed(fr):
        print(x)
