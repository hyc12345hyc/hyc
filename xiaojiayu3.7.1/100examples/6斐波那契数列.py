# 题目：斐波那契数列。
# 程序分析：斐波那契数列（Fibonacci sequence），又称黄金分割数列，指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……。
# 在数学上，费波那契数列是以递归的方法来定义：

#迭代
def fib(x):
    if x == 1:
        return 0
    elif x == 2:
        return 1
    else:
        return fib(x-2)+fib(x-1)
print(fib(8))

#for循环
def fib1(x):
    a,b = 0,1
    if x == 1:
        return 0
    elif x == 2:
        return 1
    else:
        for i in range(1,x-1):
            n = a + b
            a = b
            b = n
    return n
print(fib1(8))

#迭代输出整个数列
def fib2(x):
    if x == 1:
        return [0]
    elif x == 2:
        return [0,1]
    else:
        fib3 = [0,1]
        for i in range(1,x-1):
            fib3.append(fib3[-2]+fib3[-1])#增加的新数字是原列表倒数两数字之和
        return fib3

print(fib2(8))

