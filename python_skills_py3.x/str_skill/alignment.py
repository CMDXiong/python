# -*- encoding: utf-8 -*-

# 方案1：
# 使用字符串的str.ljust(), str.rjust(), str.center()进行左，右，居中对齐
# 填充字符只能有一个，如不能写s.ljust(10, '-*')
s = 'abc'
s.ljust(10)  # 'abc       '
s.ljust(10, '*')  # 'abc*******'

# 方案2：
# 使用format()方法，传递类似'<20', '>20', '^20'参数完成同样任务, format调用的是对象的__format__方法
format(s, '<10')  # 左对齐 'abc       '
# 填充字符
format(s, '*<10')  # 'abc*******'
# 打印数字的符号, +:表示总输出符号
format(-123, '+')   # '-123'
format(-123, '>+10')   # '      -123', 但想让-在前面
format(-123, '=+10')  # '-      123'，但想填充0
format(-123, '0=+10')  # '-000000123'

format(s, '>10')  # 右对齐
format(s, '^10')  # 居中对齐


# 对齐字典
def dict_alignment(test_dict):
    wid = max(map(len, test_dict.keys()))
    for k, v in test_dict.items():
        print(k.ljust(wid), ": ", v)


if __name__ == "__main__":
    test_dict = {'lodDist': 100.0,
                 'SmallCull': 0.04,
                 'DistCull': 500.0,
                 'trilinear': 40,
                 'farclip': 477}
    dict_alignment(test_dict)


