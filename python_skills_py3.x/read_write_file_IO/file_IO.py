# -*- encoding: utf-8 -*-
# 实际案例
# 某文本文件编码格式已知（如UTF-8, GBK, BIG5），在python 2.x和python3.x中分别如何读写该文件？
# python2   python3
# str       bytes
# unicode   str

# python2.x：写入文件前对unicode编码，读入文件后对字节进行解码。
# s = u"hello, 潘雄"
# f = open('a.txt','w')
# f.write(s.encode('utf8'))
# f.flush()

# python3.x：open函数指定't'的文本模式，encoding指定编码格式,不写t也可以，默认就有t
# s = "hello, 潘雄"
# f = open('b.txt', 'wt', encoding='utf8')
# f.write(s)
# f.flush()

