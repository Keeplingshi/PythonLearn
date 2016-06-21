# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 15:58:15 2016

@author: Administrator
"""

age=20
if age>=18:
    print('your age is',age)
    print('adult')
    
age = 3
if age >= 18:
    print('your age is', age)
    print('adult')
else:
    print('your age is', age)
    print('teenager')
    
age = 3
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')
print('==================================')

#只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False。
x=1;
if x:
    print('True')
print('==================================')

s=input('birth:')
birth=int(s)
if birth<2000:
    print('00前')
else:
    print('00后')
