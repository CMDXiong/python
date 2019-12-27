# -*- encoding: utf-8 -*-
# 实际案例
# 某软件要求,从网络抓取各个城市气温信息, 并依次显示:
# 北京: 15~20
# 天津: 17~22
# 长春: 12~18
# ...
# 如果一次抓取所有城市再显示,显示第一个城市气温时,有很高的延时, 并且浪费存储空间,我们期望以"用时访问"的策略,
# 并且能把所有城市气温封装到一个对象里, 可用for语句进行迭代. 如何解决
from collections import Iterator, Iterable
import requests


# 迭代器要实现__next__方法
class WeatherIterator(Iterator):
    def __init__(self, cities):
        self.cities = cities
        self.index = 0

    def __next__(self):
        if self.index == len(self.cities):
            raise StopIteration
        city = self.cities[self.index]
        self.index += 1
        return self.get_weather(city)

    def get_weather(self, city):
        url = 'http://wthrcdn.etouch.cn/weather_mini?city=' + city
        r = requests.get(url)
        data = r.json()['data']['forecast'][0]
        return city, data['high'], data['low']


# 可迭代对象要实现__iter__方法
class WeatherIterable(Iterable):
    def __init__(self, cities):
        self.cities = cities

    def __iter__(self):
        return WeatherIterator(self.cities)


def show(w):
    for x in w:
        print(x)


if __name__ == "__main__":
    # 以下WeatherIterator也可以实现功能, 但为何要实现WeatherIterable
    # 因为WeatherIterator迭代一次后就失效,不能再次使用
    # 而WeatherIterable是每次都返回一个新的WeatherIterator, 可以重复使用
    w = WeatherIterable(['北京', '上海', '广州'])
    # w = WeatherIterator(['北京', '上海', '广州'])
    show(w)
