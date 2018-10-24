g = lambda x,y=3 : x * y
print(g(4,6))
print('---------')

def iss(x):
    if x % 2:
        return x
    else:
        return None
print(iss(8))
print('---------')


#利用filter()和lambda表达式快速求出100以内所有3的倍数
print(list(filter(lambda x :x % 3 == 0,range(1,100))))
#或者
print(list(filter(lambda x :not x % 3,range(1,100))))
print('---------')
#用列表推导式代替filter()和lambda表达式
print([x for x in range(1,100) if x % 3 == 0])
print('---------')

#使用zip会将两数以元组的形式绑定在一块
print(list(zip([1,3,5,7,9],[2,4,6,8,10])))
#若希望是列表形式而不是元组，可采用map和lambda表达式
print(list(map(lambda x,y:[x,y],[1,3,5,7,9],[2,4,6,8,10])))
print('---------')

#以下表达式会打印什么？
def make_repeat(n):
    return lambda s : s * n

double = make_repeat(2)
print(double(8))#16
print(double('hyc'))#hychyc
