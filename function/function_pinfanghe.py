#-*- coding:utf:8 -*-
#计算输入数字的平方和

def cal(*nums):
    s = 0
    for i in nums:
        s = s + i * i
    print s


while True:
    x= (raw_input('enter:'))
    xlist = x.split(',')
    for i in range(len(xlist)):
        xlist[i] = int(xlist[i])
    cal(*xlist)