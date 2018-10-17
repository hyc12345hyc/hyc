#0下面程序会输出什么：
#python可以向前引用
def next():
    print('the first one')
    pre()
def pre():
    print('the secend one')
next()
print('-----')

