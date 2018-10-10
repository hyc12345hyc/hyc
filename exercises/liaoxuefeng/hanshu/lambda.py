# -*- coding:utf -*-
#匿名函数lambda x: x * x实际上就是：def f(x): return x * x

def xc(x):
    return lambda x:x * x
print xc(4)(4)          #xc(4)是一个函数，xc(4)(4)返回函数值
print xc(4)             #返回函数

def build1(x,y):
    return lambda x,y: x * x + y * y
print build1(123,321)(4,5)              #与第一个括号值无关

def build2():
    return lambda x,y: x * x + y * y
print build2()(5,5)

pl=lambda x:x * x                       #pl是一个函数
print pl(3)

def build3(x,y):
    return lambda : x * x + y * y
print build3(4,5)()

def build4(x,y,z):
    return lambda :x * x + y * y + z
print build4(4,5,9)()

def build5():
    return lambda x,y,z:x * x + y * y + z
print build5()(4,5,9)
