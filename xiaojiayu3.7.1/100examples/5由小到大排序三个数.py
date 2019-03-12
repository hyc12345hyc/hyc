# 题目：输入三个整数x,y,z，请把这三个数由小到大输出。

x = int(input("请输入整数X："))
y = int(input("请输入整数Y："))
z = int(input("请输入整数Z："))
list = [x,y,z]
list.sort()
for i in range(0,3):
    print(list[i])