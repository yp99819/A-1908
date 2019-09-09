#!/usr/bin/env python
# -*- coding: utf-8 -*-

#__title__ = ''
#__author__ = 'yupeng'
#__mtime__ = '2019/9/5'


# 新增单个数据
l = [1,2,3,4,5,6,7,8,9]
l.append(97)
print(l)

# 在列表中的某个位置新增单个数据
l.insert(3,97)
print(l)

# 在列表最后新增多个数据
y = [9,9,7,7]
l.extend(y)
print(l)
print(y)

# 删除单个数据
print(l.pop())
print(l)
print(l.pop(9))
print(l)
print(l.pop(-1))
print(l)

# 根据内容删除数据
l.remove(9)
print(l)

# 根据下标修改列表中的数据
l[6]=97
print(l)

# 长度
print(len(l))

# 排序 正序
l.sort()
print(l)

# 倒序  reverse 排序规则 False 升序(默认)  True 降序
l.sort(reverse=True)
print(l)

