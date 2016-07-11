# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 14:33:08 2016

@author: Administrator
"""

import math

print(abs(100))
print(abs(-20))
print(abs(12.34))

print(max(2, 3, 1, -5))

print(str(1.23))

# hex()函数把一个整数转换成十六进制表示的字符串
print(hex(17))

# 函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”
a=abs
print(a(-1))

print("======================================")

#自定义函数
def my_abs(x):
    if x>=0:
        return x
    else:
        return -x

print(my_abs(-20))

# 空函数：pass语句什么都不做，那有什么用？实际上pass可以用来作为占位符，
# 比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来。
def nop():
    pass

#pass还可以用在其他语句里
#缺少了pass，代码运行就会有语法错误。
age=20
if age>=18:
    pass

#数据类型检查可以用内置函数isinstance()实现
def my_abs2(x):
    if not isinstance(x, (int, float)):
        print('bad operand type')
        return
    if x >= 0:
        return x
    else:
        return -x
        
print(my_abs2(a))


#函数可以同时返回多个值，但其实就是一个tuple
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

r = move(100, 100, 60, math.pi / 6)
print(r)