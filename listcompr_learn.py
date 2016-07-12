# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 14:09:12 2016

@author: Administrator
"""

#列表生成式
import os


L=list(range(1,11))
print(L)

#生成[1x1, 2x2, 3x3, ..., 10x10]
L=[x*x for x in range(1,11)]
print(L)


L=[x * x for x in range(1, 11) if x % 2 == 0]
print(L)

L=[m+n for m in 'ABC' for n in 'XYZ']
print(L)

#列出当前目录下的所有文件和目录名
L=[d for d in os.listdir('.')]
print(L)

d = {'x': 'A', 'y': 'B', 'z': 'C' }
L=[k + '=' + v for k, v in d.items()]
print(L)

L = ['Hello', 'World', 'IBM', 'Apple']
t=[s.lower() for s in L]
print(t)