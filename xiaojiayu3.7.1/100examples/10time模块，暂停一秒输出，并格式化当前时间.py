#题目：暂停一秒输出，并格式化当前时间。

#相关资料http://www.runoob.com/python3/python3-date-time.html
import time
a = time.time()
print("当前时间戳为:", a)
b = time.localtime()
print("本地时间为 :",b)
c = time.asctime()
print("简单格式化的本地时间为 :",c)
d = time.mktime(time.localtime())
print(d)


for i in range(10):
    c = time.asctime()
    print("本地时间 :", c)
    time.sleep(1)

#我们也可以使用 time 模块的 strftime 方法来格式化日期
# 格式化成2016-03-20 11:45:39形式
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# 格式化成Sat Mar 28 22:24:24 2016形式
print (time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))

import calendar

cal = calendar.month(2016, 1)
print ("以下输出2016年1月份的日历:")
print (cal)
