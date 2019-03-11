#函数嵌套示例
def f1():
    def f2():
        def f3():
            print('from f3')
        f3()
        print('from f2')
    f2()
    print('from f1')
f1()
print('---------')

#global关键字举例
#在函数中修改全局变量的值
count = 10
def f():
    global count
    count = 5
    print(count)
f()
print(count)
print('---------')

#nonlocal关键字举例
#在嵌套的函数中，在内部函数修改外部函数的局部变量
def f():
    x = 5
    def g():
        nonlocal x
        x *= x
        return x
    return g()

print(f())
print('---------')


def out1():
    v = 4
    def in1():
        nonlocal v
        print(v)
        v = 3
    in1()
out1()
