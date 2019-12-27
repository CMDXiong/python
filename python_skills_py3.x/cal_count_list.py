# -*- encoding: utf-8 -*-
# 统计序列中元素的频度
# 实际案例
# 1.某随机序列[12, 5, 6, 4, 6, 5, 5, 7]中, 找到出现次数最高的3个元素,它们出现次数是多少?
# 2.对某英文文章的单词,进行词频统计, 找到出现次数最高的10个单词,它们出现次数是多少?

# 方案1: 将序列转换为字典{元素:频度}, 根据字典中的值排序

from random import randint
data = [randint(0, 20) for _ in range(30)]
d =dict.fromkeys(data, 0)
for x in data:
    d[x] += 1
res = sorted(d.items(), key=lambda item: item[1], reverse=True)[0: 5]  # 取前5
res = sorted(((v, k) for k, v in d.items()), reverse=True)[0: 5]  # 取前5
print(res)

# 如果d很大, 只取前5, 使用整体排序是五种浪费, 所以应该使用堆
import heapq
res2 = heapq.nlargest(5, ((v, k) for k, v in d.items()))
print(res2)

# 方案2:使用标准库collections中的Counter对象
from collections import Counter
c = Counter(data)
res3 = c.most_common(5)  # 取频度最高的5个数
print(res3)

