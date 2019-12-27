# -*- encoding: utf-8 -*-
# 迭代多个可迭代对象
# 实际案例
# （并行）1.某班学生期末考试成绩，语文， 数学，英语分别存储在3个列表中，同时迭代三个列表，计算每个学生的总分
# （串行）2.某年级有4个班，某次考试每班英语成绩分别存储在4个列表中，依次迭代每个列表，统计全学年成绩高干90分人数

# 解决方案
# 并行：使用内置函数zip，它能将多个可迭代对象合并，每次迭代返回一个元组

from random import randint
chinese = [randint(60, 100) for _ in range(20)]
math = [randint(60, 100) for _ in range(20)]
english = [randint(60, 100) for _ in range(20)]

res1 = [sum(s) for s in zip(chinese, math, english)]
res2 = list(map(sum, zip(chinese, math, english)))
res3 = list(map(lambda s1, s2, s3: s1+s2+s3, chinese, math, english))
print(res1, res2, res3)

# 串行：使用标准库中的itertools.chain, 它能将多个可迭代对象连接
from itertools import chain

res4 = len([x for x in chain(chinese, math, english)])
print(res4)

# 比较复杂的例子
s = 'abc;123|xyz;678|fskjgd\tjsdf'
from functools import reduce

res5 = list(reduce(lambda it_s, sep: chain(*map(lambda ss: ss.split(sep), it_s)), ';|\t', [s]))
print(res5)
