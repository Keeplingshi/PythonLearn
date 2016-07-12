# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 16:24:30 2016

@author: Administrator
"""

def f(x):
    return x * x

print(list(map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

#再看reduce的用法。reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
#reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

from functools import reduce
def add(x,y):
    return x+y
    
print(reduce(add,[1,3,5,7,9]))


def normalize(name):
    s=name.capitalize()
    return s    
    
L1 = ['adam', 'LISA', 'barT']
print(list(map(normalize,L1)))
