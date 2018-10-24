#斐波那契数列 迭代法
def fib(n):
    a = 1
    b = 1
    c = 1
    if n < 1:
        print('输入有误：')
        return -1
    while (n-2) > 0:
        c = a + b
        a = b
        b = c
        n -= 1
    return c
print(fib(30))

#斐波那契数列 递归法
def fib1(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return fib1(n-1) + fib1(n-2)

print(fib1(30))
print('---------')
