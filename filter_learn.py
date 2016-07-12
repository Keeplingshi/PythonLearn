# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 16:47:38 2016

@author: Administrator
"""

#Python内建的filter()函数用于过滤序列
#filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素
def is_odd(n):
    return n%2==1
    
print(list(filter(is_odd,[1,2,3,4,5,6,7,8,9])))

def is_palindrome(n):
    s=str(n)
    slen=len(s)
    i=0
    while i<slen:
        if s[i]!=s[-(i+1)]:
            return False
        i=i+1
    return True
    
output = filter(is_palindrome, range(1, 1000))
print(list(output))


