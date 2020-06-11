from collections.abc import Iterator, Iterable


class MyIterator(Iterator):
    def __init__(self, my_list):
        self.container = my_list
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            ret = self.container[self.index]
        except IndexError:
            raise StopIteration
        self.index += 1
        return ret


class Mylist(object):
    def __init__(self, new_list):
        self.container = new_list
        self.index = 0

    def add(self, item):
        self.container.append(item)

    # 用迭代器来维护数状态
    def __iter__(self):
        return MyIterator(self.container)


if __name__ == '__main__':
    # main()
    mylist = Mylist([1, 2, 3])
    my_itor = iter(mylist)
    while True:
        try:
            print(next(my_itor))
        except StopIteration:
            break

    for it in mylist:
        print(it)
