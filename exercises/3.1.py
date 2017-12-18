# -*- coding:utf-8 -*-
#一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
t = []
for m in range(168):
    for n in range(m):
        if m ** 2 - n ** 2 == 168:
            x = n ** 2 - 100
            t.append(x)
print'符合条件的整数有：',t