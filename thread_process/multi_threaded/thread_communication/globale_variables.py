# coding=utf-8
# 线程间的全局变量如果过多，可以放在一个文件中统一管理
# 使用全局文件来管理全局变量时，需要特别注意
# 不能使用from globale_variables import detail_url_list这种方式，如果仅仅是读取，没有问题
# 因为如果一个线程对detail_url_list修改后，其他的线程并不能发现这个改变
detail_url_list = []