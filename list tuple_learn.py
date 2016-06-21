# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 15:26:26 2016

@author: Administrator
"""

#list。list是一种有序的集合，可以随时添加和删除其中的元素。
classmates=['Michael','Bob','Tracy']
print(classmates)
print(len(classmates))
print(classmates[0])
print(classmates[1])
print(classmates[-1])

classmates.append('Adam')
print(classmates)

classmates.insert(1,'Jack')
print(classmates)

classmates.pop()
print(classmates)

classmates[1]='Sarah'
print(classmates)
print('==================================')

L=['Apple',123,True]
print(L)

s=['python','java',['asp','php'],'scheme']
print(s)
print(len(s))

L=[]
print(len(L))
print('==================================')

#另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改
tupletest=('Michael','Bob','Tracy')
#tupletest[0]='4111'   会报错
print(tupletest)
#重新赋值
tupletest=()
print(tupletest)

#所以，只有1个元素的tuple定义时必须加一个逗号,，来消除歧义
#t = (1)不是tuple，t=(1,)才是
t=(1,)
print(t)

#tuple中的list，list可变
t = ('a', 'b', ['A', 'B'])
t[2][0]='X'
t[2][1] = 'Y'
print(t)
print('==================================')

test = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
print(test[0][0])
print(test[1][1])
