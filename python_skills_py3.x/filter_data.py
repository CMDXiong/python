from random import randint

# 以下都推荐使用第一种方式，速度更快，也更简单

# 列表  过滤出>=0的数据
l = [randint(-10, 10) for _ in range(10)]
l_filter1 = [x for x in l if x >= 0]               # 1.使用列表生成式
l_filter2 = list(filter(lambda x: x >= 0, l))      # 2.使用filter函数
print(l_filter1, l_filter2)

# 字典 过滤出分数>=90的人数
dic = {'student%d' % i: randint(50, 100) for i in range(1, 21)}
dic_filter1 = {k: v for k, v in dic.items() if v >= 90}
dic_filter2 = dict(filter(lambda item: item[1] >= 90, dic.items()))
print(dic_filter1, dic_filter2)

# 集合 过滤出能被3整除的数
s = {randint(0, 20) for _ in range(20)}
s_filter1 = {x for x in s if x % 3 == 0}
s_filter2 = set(filter(lambda x: x % 3 == 0, s))
print(s_filter1, s_filter2)
