#0 计算打印所有参数的和乘以基数（base = 3）的结果
# 如果参数中最后一个参数为（base = 5），则设定基数为5，基数不参与求和计算
def test(*prams,base = 3):
    if base == 5:
        print(sum(prams)*5)
    else:
        print(sum(prams)*base)
    print("-------")
test(2,3,4,5,6,7,base=5)



# 1 寻找水仙花数
# 要求：如果一个三位数等于其各位数字的立方和，则称这个数为水仙花数。列如153。编写一个程序，找出所有的水仙花数。
def shuixian0():
    for x in range(100,1000):
        if x == (x//100)**3 + (x//10%10)**3 + (x%10)**3:
            print(x)
    print("-------")
def shuixian1():
    for x in range(1,10):
        for y in range(10):
            for z in range(10):
                if x*100 + y*10 + z == x**3 + y**3 + z**3:
                    print(x*100 + y*10 + z)
    print("-------")
shuixian0()
shuixian1()


# 2.编写一个函数findstr（），该函数统计一个长度为2的子字符串在另一个字符串中出现的次数。
# 例如：假定目标字符串为“”，子字符串为“”，函数执行后打印“子字符串在目标字符串中共出现 次”
def findstr(x,y):#x目标字符串，y子字符串
    count = 0
    if y not in x:
        print('子字符串不在目标字符串内')
    else:
        for i in range(len(x)-1):
            if x[i] == y[0]:
                if x[i+1] == y[1]:
                    count += 1
        print('子字符串在目标字符串中共出现',count,'次')

findstr('abccabcccaaaccacaaaac','cc')