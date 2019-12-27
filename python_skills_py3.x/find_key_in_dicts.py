# -*- encoding: utf-8 -*-
# 如何快速找到多个字典中的公共键
# 实际案例
# 西班牙足球甲级联赛,每轮球员进球统计:
# 第1轮:{'苏亚雷斯': 1, '梅西':2, '本泽马':1, ...}
# 第2轮:{'苏亚雷斯': 3, 'C罗':2, '格里兹曼':1, ...}
# 第3轮:{'苏亚雷斯': 1, '梅西':2, '贝尔':1, ...}
# ...

# 统计出前N轮, 每场比赛都有进球的球员
# 方案1
from random import randint, sample
d1 = {k: randint(1, 4) for k in sample("abcdefg", randint(3,6))}
d2 = {k: randint(1, 4) for k in sample("abcdefg", randint(3,6))}
d3 = {k: randint(1, 4) for k in sample("abcdefg", randint(3,6))}

d_l = [d1, d2, d3]
res = [k for k in d_l[0] if all(map(lambda d: k in d, d_l[1:]))]
print(res)

# 方案2
# 利用集合(set)的交集操作
# step1: 使用字典的keys()方法,得到一个字典keys的集合.
# step2: 使用map函数, 得到每个字典keys的集合
# step3: 使用reduce函数,取所有字典的keys集合的交集

from functools import reduce
res2 = reduce(lambda a, b: a&b, map(dict.keys, d_l))
print(res2)


