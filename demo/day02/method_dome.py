#!/usr/bin/env python
# -*- coding: utf-8 -*-

#__title__ = ''
#__author__ = 'yupeng'
#__mtime__ = '2019/9/5'




# 无参数、无返回值的方法
# 方法的定义( def )
def jia_fa():
    a = 1
    b = 2
    print(a+b)
# 方法的调用
jia_fa()


# 有参数、无返回值的方法
# 方法的定义( def )
def jia_fa2(a,b):
    print(a+b)
# 直接调用
jia_fa2(4,4)
jia_fa2(11,89)


# 无参数、有返回值的方法
def jia_fa():
    a = 1
    b = 2
    return a + b
# 调用
c = jia_fa()
print(c)


# 有参数、有返回值
def jia_fa(a,b):
    return a + b

c = jia_fa(1,3)
print(c)
c = jia_fa(1234,7945)
print(c)



def ppp(y,p=10000):
    return y + p
print(ppp(1))
print(ppp(100,100))
print(ppp(1000,p=1))


def yyy(*args,**kwargs):
    print(args)
    print(kwargs)

yyy(11,22,33,44,55,y=9,p=7)





