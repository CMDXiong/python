# -*- encoding: utf-8 -*-
# 字典按其值排序

# 实际案例
# 某班英语成绩以字典形式存储为：
# {
#     'Lilei': 79,
#     'Jim': 88,
#     'Lucy': 92,
#     ...
# }
# 如何根据成绩高低，计算学生排名

# 解决方案
# 方案1: 将字典中的各项转换为(值,键)元组,(列表解析或zip),元组可以比较大小
from random import randint
d = {k: randint(60, 100) for k in 'abcdefgh'}
l = [(v, k) for k, v in d.items()]
res = sorted(l, reverse=True)
print(res)

res2 = sorted(list(zip(d.values(), d.keys())), reverse=True )
print(res2)

# 方案2:传递sorted函数的key参数
res3 = sorted(d.items(), key=lambda item:item[1], reverse=True)
print(res3)