#使用递归编写一个power()函数模拟内减函数pow()，即power(x,y)为计算并返回x的y次幂的值
def power(x,y):
    if y == 1:
        return x
    else:
        return x * power(x,y-1)
print(power(3,4))
print('---------')

#使用递归编写一个函数，利用欧几里得算法求最大公约数，即gcd(x,y)返回值为参数x和参数y的最大公约数
def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x%y)
print(gcd(12,18))
print('---------')


#普通函数
def qiu(x):
    n = x
    for i in range(1,x):
        n = n * i
    return n

result = int(input('请输入正整数：'))
print('%d的阶乘是%d'% (result,qiu(result)))

#递归
def qiu1(y):
    if y == 1:
        return 1
    else:
        return y * qiu1(y-1)

result = int(input('请输入正整数：'))
print('%d的阶乘是%d'% (result,qiu(result)))
print('---------')

