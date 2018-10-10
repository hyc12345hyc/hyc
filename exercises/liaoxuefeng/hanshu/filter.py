# -*- coding: UTF-8 -*-
#检查输入的数字是不是素数

while True:
    x = int(raw_input("请输入数字："))

    if x > 1:
        for i in range(2,x):
            if x % i == 0:
                print(x,'is not a prime number')
                print(i,"*",x/i)
                break
        else:
            print(x,"is a prime number")
    else:
        print(x,"is not a prime number")



