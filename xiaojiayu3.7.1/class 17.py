# 0. 编写一个函数power()模拟内建函数pow()，即power(x, y)为计算并返回x的y次幂的值。
def power(x,y):
    return x ** y

def power1(x,y):
    result = 1
    for i in range(y):
        result = result * x
    return result

print(power(3,4))
print("-------")
print(power1(3,4))
print("-------")



#1. 编写一个函数，利用欧几里得算法求最大公约数，例如gcd(x, y)返回值为参数x和参数y的最大公约数。

#标准答案
def gcd1(x, y):
    while y:
        t = x % y
        x = y
        y = t
    return x

print(gcd1(12, 16))
print("-------")


def gcd(x,y):
    list1 = [max(x,y),min(x,y)]                #大数在前
    while list1[-2] % list1[-1] != 0:
        list1.append(list1[-2] % list1[-1])    #循环将余数加入列表末尾，直到余数为零
    return list1[-1]
print(gcd1(12, 16))
print("-------")


