# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 16:31:47 2016

@author: Administrator
"""

#字典,dict内部存放的顺序和key放入的顺序是没有关系的
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])

d['Adam'] = 67
print(d)

#通过in判断key是否存在
print('Tomas' in d)
if 'Tomas' in d:
    print('yes')
else:
    print('no')

#通过dict提供的get方法，如果key不存在，可以返回None，或者自己指定的value
print(d.get('Thomas'))
print(d.get('Thomas',-1))

#删除一个key
d.pop('Bob')
print(d)
print('=======================================')


#要创建一个set，需要提供一个list作为输入集合
s = set([1, 2, 3])
print(s)
s = set([1, 1, 2, 2, 3, 3])
print(s)
s.add(4)
print(s)
s.remove(1)
print(s)
s.pop()
print(s)
