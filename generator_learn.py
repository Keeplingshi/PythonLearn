# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 14:30:11 2016

@author: Administrator
"""

#generator生成器
g=(x*x for x in range(10))
print(g)    #输出的并不是数字，而是<generator object <genexpr> at 。。。
#如果要一个一个打印出来，可以通过next()函数获得generator的下一个返回值
#print(next(g))
#print(next(g))

#也可以使用for循环打印g
for n in g:
    print(n)

print('=======================================')
#这就是定义generator的另一种方法。如果一个函数定义中包含yield关键字，
#那么这个函数就不再是一个普通函数，而是一个generator
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'
    
f=fib(6)
#print(next(f))
#print(next(f))
#print(next(f))

for n in fib(6):
    print(n)

