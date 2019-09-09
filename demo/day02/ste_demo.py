#!/usr/bin/env python
# -*- coding: utf-8 -*-

#__title__ = ''
#__author__ = 'yupeng'
#__mtime__ = '2019/9/5'


# 截取
def aa():
    a = 'dgsdfaafsad'
    # 截取其中一段
    print(a[1:5])
    print(a[5:])
    print(a[:7])
    print(a[:-2])
    print(a[::-1])   # 字符串倒叙排列



# draiegko 要求生成两个新的字符串  drai  和  egko
def bb():
    b = 'dergalio'
    print(b[::2])
    print(b[1::2])

# 通过下标取出字符串中的字符
def cc():
    b = 'dergalio'
    print(b[2])

# 重复字段
def dd():
    b = 'dergalio'
    print(b * 5)

# 字符串切片
def ee():
    d = '名字,姓名,性别'
    print(d.split(","))

# 去空格
def qq():
    d = '   dsadsadas   '
    print(d.strip())
    # print(d.ltrip)  # 去左边的空格

# 替换
def ww():
    d = 'sadsadfs"d232dsa'
    print(d.replace("'",'"'))

# 查找
def rr():
    d = 'guoyasoft'
    print(d.find("ya"))

# 长度
def tt():
    d = 'guoyasoft'
    print(len(d))

# 练习题
def yy():
    d = 'GET https://www.fiddler2.com/UpdateCheck.aspx?isBeta=False HTTP/1.1'
    print(d.split(" "))
    l = d.split(" ")
    method = l[0]
    print("请求方法：" +method)
    banben = l[2]
    print("协议版本：" +banben)


    # print(d(scheme='http', netloc='www.chenxm.cc', path='/post/719.html', params='', query='', fragment=''))

if __name__ == '__main__':
    yy()


