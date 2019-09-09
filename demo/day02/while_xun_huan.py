#!/usr/bin/env python
# -*- coding: utf-8 -*-

#__title__ = ''
#__author__ = 'yupeng'
#__mtime__ = '2019/9/5'


# while 循环
'''
i = 0
while(判断条件):
    循环体
    i=i+1
'''

# 显示1-100
def xian_shi():
    i = 1
    while(i < 101):
        print(i)
        i += 1 #  i = i + 1

# 监听(进入死循环一直监听)
def si_xun_huan():
    while(True):
        pass



if __name__ == '__main__':
    xian_shi()
