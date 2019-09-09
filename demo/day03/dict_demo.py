#!/usr/bin/env python
# -*- coding: utf-8 -*-

#__title__ = ''
#__author__ = 'yupeng'
#__mtime__ = '2019/9/6'



'''
key:value

key 是 唯一的
key 必须是不可变的(数字、字符串、元组)    不可修改(列表、字典)

'''


# 增
# 初次创建

d = {}
d1 = {"name":"小花同学","sex":"女"}
# 新增一对数据
d1['age'] = 18
d1['student_id'],d1['song'] = 9,'让晚风轻轻吹送了晚霞'
print(d1)

# 删
# 删除key
print(d1.pop('student_id'))
print(d1)
print(d1.pop('age'))
print(d1)
# 改     修改和新增是一样 如果里面没有这个key就新增一个key 有key就是修改值
d1['name'] = '小花'
print(d1)

# 查
print(d1['name'])

# 获取一个字典的长度
print(len(d1))

# 成员判断 /只能用 key 做判断
print('name' in d1)

# 字典的拼接

d2 = {1:'11',2:'22'}

d3 = {3:'33',4:'44'}
# 在某个字典末尾加上另一个字典
# 拿着 d3 修改 d2 ，key 有则改value, 无则新增
d2.update(d3)
print(d2)




