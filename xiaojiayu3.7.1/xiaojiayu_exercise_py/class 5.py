#1. 写一个程序，判断给定年份是否为闰年。（注意：请使用已学过的 BIF 进行灵活运用）
# 这样定义闰年的:能被4整除但不能被100整除,或者能被400整除都是闰年。


year = input("请输入年份,输入0退出：")
while not year.isdigit():
    print("你输入的不是年份，请重新输入")
    year = input("请输入年份，输入0退出：")
while int(year) :
    if (((int(year) % 4 == 0) and (int(year) % 100 != 0)) or (int(year) % 400 == 0)):
        print(year+"是闰年")
    else:
        print(year+"不是闰年")
    year = input("请输入年份，输入0退出：")



#s为字符串
#s.isalnum()  所有字符都是数字或者字母，为真返回 Ture，否则返回 False。
#s.isalpha()   所有字符都是字母，为真返回 Ture，否则返回 False。
#s.isdigit()     所有字符都是数字，为真返回 Ture，否则返回 False。
#s.islower()    所有字符都是小写，为真返回 Ture，否则返回 False。
#s.isupper()   所有字符都是大写，为真返回 Ture，否则返回 False。
#s.istitle()      所有单词都是首字母大写，为真返回 Ture，否则返回 False。
#s.isspace()   所有字符都是空白字符，为真返回 Ture，否则返回 False。