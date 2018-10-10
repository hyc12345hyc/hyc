#0. 还记得我们第一讲的动动手的题目吗？这一次要求使用变量，计算一年有多少秒？
#提示：可以以 DaysPerYear（每年天数），HoursPerDay（每天小时数），MinutesPerHour（每小时分钟数），SecondsPerMinute（每分钟秒数）为变量名。

dpy = 365
hpd = 24
mph = 60
spm =60
seconds = dpy*hpd*mph*spm
print (seconds)

#除了使用反斜杠（\）进行字符转义，还有什么方法可以打印：Let's go! 这个字符串？
print("Let's go!")

#如果非要在原始字符串结尾输入反斜杠，可以如何灵活处理？
sen = r'C:\Program Files\FishC\Good''\\'
print (sen)