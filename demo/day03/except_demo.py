#!/usr/bin/env python
# -*- coding: utf-8 -*-

#__title__ = ''
#__author__ = 'yupeng'
#__mtime__ = '2019/9/6'


def d(a,b):
    try:
        c = a/b
    except ZeroDivisionError:
        print("除数不能为0")
        return
    return c

print(d(99,3))



def w():
    try:
        open("test","r")
        g = open("test.txt","w")
        g.read()
        g.close()
        g.write("ssss")
    except FileNotFoundError:
        print("文件不存在")
    except ValueError:
        print("文件已关闭")

w()









