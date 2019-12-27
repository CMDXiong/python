# -*- encoding: utf-8 -*-
# 让字典保持有序
# 实际案例
# 某编程竞赛系统,对参赛选手编程钥匙进行计时,选手完成 题目后,把该 选手解题用时记录到字典中,以便赛后按选手名查询成绩.
# {'Lilei': (2,43), "HanMeimei": (5, 52), 'Jim':(1, 39) ...}
# 比赛结束后,需按排名顺序依次打印选手成绩,如何实现

# 字典中的顺序是无序的: 输入字典与迭代的字典顺序通常不一致
# 实现有顺的字典:
# 解决方案:
# 使用标准库collections 中的OrderedDict
from collections import OrderedDict
from itertools import islice
od = OrderedDict()
player = list('abcdefgh')
from random import shuffle
shuffle(player)
for i, p in enumerate(player, 1):
    od[p] = i


def query_by_name(d, name):
    return d[name]


def query_by_order(d, a, b= None):
    a -= 1
    if b is None:
        b = a+1
    return list(islice(od, a, b))


print(query_by_order(od, 3, 6))


