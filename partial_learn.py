# -*- coding: utf-8 -*-
"""
Created on Sat Jul 16 14:59:21 2016

@author: Administrator
"""

#偏函数
import functools
int2=functools.partial(int,base=2)
print(int2('1000000'))

#简单总结functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。
