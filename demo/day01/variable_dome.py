#!/usr/bin/env python
# -*- coding: utf-8 -*-

#__title__ = '有什么类型'
#__author__ = 'yupeng'
#__mtime__ = '2019/9/4'

# 有哪些类型
'''

int
float
list
tuple
dict
None
bool
str

'''

# 变量名是什么
# = 是赋值符
# type 是方法名
# 需要一个变量作为参数
# type()  方法的作用是来查看变量的类型

a = '''aaaaa"bbbbb'''
print(type(a))

# list 列表 [开始   ]结束 ， 中间多个值用英文逗号隔开
b = [1,]
print(type(b))

# tuple 元组  (开始   )结束，中间多个值用英文逗号隔开， 如果元组中只有单个值， 在参数后面加个逗号结尾
c = (1,)
print(type(c))

# dict字典类型 哈希   {开始   }结束，存成对的值(类似键值对), kay: value 多对值用逗号隔开
d = {'name':'呜呜呜呜','年龄':24}
print(d)
print(type(d))

# 取下标
f = [1,2,3,4,5,6]
print(f[4])




