# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 10:02:38 2016

@author: Administrator
"""

#切片功能
#取一个list或tuple的部分元素是非常常见的操作
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print(L[1:3])
print(L[-3:-1])
print(L[-1])

print('===================================')
L = list(range(100))
print(L[:10:2]) #前10个数，每两个取一个
print(L[::5])   #所有数，每5个取一个
print(L[:])     #只写[:]就可以原样复制一个list

#tuple也可以用切片操作
#字符串'xxx'也可以看成是一种list,字符串也可以用切片操作
print((0, 1, 2, 3, 4, 5)[:3])
print('ABCDEFG'[:3])

