#0. 编写程序：hello.py，要求用户输入姓名并打印“你好，姓名！”
name = input("请输入姓名：")
print("你好，" + name + "!")

#1. 编写程序：calc.py 要求用户输入1到100之间数字并判断，输入符合要求打印“你妹好漂亮”，不符合要求则打印“你大爷好丑”

answer = 10
number = int(input("请输入1到100之间数字:"))
while number != answer:
    number = int(input("请输入1到100之间数字:"))
    if number == answer:
        print("你妹好漂亮")
    else:
        print("你大爷好丑")
print("DONE")