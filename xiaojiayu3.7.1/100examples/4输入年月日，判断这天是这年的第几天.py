# 题目：输入某年某月某日，判断这一天是这一年的第几天？

list = [31,28,31,30,31,30,31,31,30,31,30,31]
list_leap = [31,29,31,30,31,30,31,31,30,31,30,31]
year =  int(input('请输入年份：'))
month = int(input('请输入月份：'))
date =  int(input('请输入日期：'))
d = 0
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    for i in range(0, month - 1):
        d += list_leap[i]
    day = d + date
    print(day)
else:
    for i in range(0, month - 1):
        d += list[i]
    day = d + date
    print(day)


