#0视频中小甲鱼使用 if elif else 在大多数情况下效率要比全部使用 if 要高。
#但根据一般的统计规律，一个班的成绩一般服从正态分布，也就是说平均成绩一般集中在 70~80 分之间，因此根据统计规律，我们还可以改进下程序以提高效率。
#题目备忘：按照100分制，90分以上成绩为A，80到90为B，60到80为C，60以下为D，写一个程序，当用户输入分数，自动转换为ABCD的形式打印。

temp = int(input("输入成绩："))
while temp:
    if 60 <= temp < 80:
        print("成绩为C！")
    elif 80 <= temp < 90:
        print("成绩为B！")
    elif 90 <= temp <=100:
        print("成绩为A！")
    elif 0 <= temp <=60:
        print("成绩为D！")
    else:
        print("输入错误！")
    temp = int(input("输入成绩："))



