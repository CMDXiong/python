# -*- encoding: utf-8 -*-

# 为元组中的每个值名称

# 实际案例
# 学生信息系统中数据为固定格式:(名字，年龄， 性别， 邮箱)
# ('Jim', 16, 'male', 'jim8721@gmail.com')
# ('LiLei', 17, 'male', 'leile@qq.com')
# ('Lucy', 16, 'female', 'lucy123@yayoo.com')
# 访问时，我们使用索引（index）访问，大量索引降低程序可读性.
# 比如：以下代码索引1，2降低了程序可读性
# def xxx_func(student):
#     if student[1] < 18:
#         pass
#     if student[2] == 'male':
#         pass
#     # ...
# student = ('Jim', 16, 'male', 'jim8721@gmail.com')
# xxx_func(student)

# 解决方案
# 方案1：定义一系列数值常量或枚举类型，使得数值变得有意义
# NAME, AGE, SEX, EMALE = range(4)
# def xxx_func(student):
#     if student[AGE] < 18:
#         pass
#     if student[SEX] == 'male':
#         pass
#     # ...
# student = ('Jim', 16, 'male', 'jim8721@gmail.com')
# xxx_func(student)

# 另外一个需求：如果老师信息的格式为(34, 'liushuo', 'liushuo@qq.com', 'female'), 上面的常量值就不能用了，
# 可以使用植枚举类型，分别为老师和学生创建不同的枚举
# from enum import IntEnum
# class StudentEnum(IntEnum):
#     NAME = 0
#     AGE = 1
#     SEX = 2
#     EMAIL = 3
#
# class TeacherEnum(IntEnum):
#     AGE = 0
#     NAME = 1
#     EMAIL = 2
#     SEX = 3
# def xxx_func(student):
#     if student[StudentEnum.AGE] < 18:
#         pass
#     if student[StudentEnum.SEX] == 'male':
#         pass
#     # ...
# student = ('Jim', 16, 'male', 'jim8721@gmail.com')
# xxx_func(student)
# teacher = (34, 'liushuo', 'liushuo@qq.com', 'female')
# xxx_func(teacher)

# 方案2：使用标准库中collections.namedtuple替代内置tuple, 推荐使用这种
from collections import namedtuple
Student = namedtuple('Student', ['name', 'age', 'sex', 'email'])
s1 = Student('Jim', 16, 'male', 'jim8721@gmail.com')
print(s1)
print(s1.name, s1.age, s1.sex, s1.email)
print(s1[0], s1[1], s1[2], s1[3])




