#!/usr/bin/env python
# -*- coding: utf-8 -*-

#__title__ = ''
#__author__ = 'yupeng'
#__mtime__ = '2019/9/5'



# 求出1+2+3.。。+100和
def qiu_he():
    s = 0
    for i in range(100):
        s = s + i + 1
    print(s)
# 求出100! 1*2*3*4....*100
def qiu_jie_cheng():
    s = 1
    for i in range(1,101):
        s *= i
    print(s)
# 求出100以内的质数
def zhi_shu():
    for i in range(2,101):
        if(i == 2):
            print(i)
            continue
        f = 1 # 1代表这个数是质数，0代表这个数不是质数
        for j in range(2, i):
            if (i % j == 0):
                f = 0
                break
        if(f == 1):
            print(i)


# 打印出九九乘法表（循环嵌套）
def jiu_jiu():
    for i in range(1,10):
        for j in range(1,i+1):
            print(j,"X",i,'=',i*j,"\t",end="")
        print()
# 冒泡排序
def mao_pao():
    a = [90, 43, 2, 63, 6, 3, 4]  # 列表数据
    for i in range(len(a)-1,0,-1): # 外层循环确定待排序的位置对他进行倒序排序
        for j in range(i):  # 内层循环依次取相邻的两个数据
            if (a[j] > a[j+1]):  # if判断比较相邻两个数据的大小，如果前边大于后边的，则交换位置
                a[j],a[j+1] = a[j+1],a[j]
    print(a)



if __name__ == '__main__':
    for i in range(1,10):
        for j in range(1,i+1):
            print("%a*%a=%a"%(j,i,j*i),end=" ")
        print()

