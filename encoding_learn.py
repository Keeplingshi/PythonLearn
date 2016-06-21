# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 14:57:29 2016

@author: Administrator
"""

print('包含中文的str')
print('==================================')

#在最新的Python 3版本中，字符串是以Unicode编码的
#ord()函数获取字符的整数表示
print(ord('A'))
print(ord('中'))
#chr()函数把编码转换为对应的字符
print(chr(65))
print(chr(20013))
print('==================================')

print('\u4e2d\u6587')
print('==================================')

#Python对bytes类型的数据用带b前缀的单引号或双引号表示
print('ABC'.encode('utf-8'))
print('中文'.encode('utf-8'))

print(b'ABC'.decode('ascii'))
print( b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))
print('==================================')

print(len('ABC'))
print(len('中文'))
print('==================================')

#在Python中，采用的格式化方式和C语言是一致的，用%实现
print('Hi,%s,you have $%d.' % ('chenbin',100))
print('%2d-%02d' % (3, 1))
print('==================================')

#有些时候，字符串里面的%是一个普通字符怎么办？这个时候就需要转义，用%%来表示一个%
s1 = 72
s2 = 85
r=(85-72)/72*100
print('%.1f%%' % r)
print('==================================')