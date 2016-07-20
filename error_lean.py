# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 14:45:00 2016

@author: Administrator
"""

try:
    print('try...')
    r=10/0
    print('result:',r)
except ZeroDivisionError as e:
    print('except:',e)
finally:
    print('finally...')
print('END')


print('=====================================')
try:
    print('try...')
    r = 10 / int('2')
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
else:
    print('no error!')
finally:
    print('finally...')
print('END')