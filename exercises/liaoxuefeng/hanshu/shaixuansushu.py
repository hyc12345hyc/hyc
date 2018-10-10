#-*- coding:utf-8 -*-
#筛选出列表中的素数

def f(x):
    if x > 1:
        for i in range(2,x):
            if (x % i) == 0:
                break
        else:
            print x
    else:
        pass

filter(f,range(1000))


