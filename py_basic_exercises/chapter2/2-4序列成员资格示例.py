#-*-coding:utf-*-
#检查用户名和PIN码。

datebase = [
    ['abc','123'],
    ['def','456'],
    ['ghi','789'],
]
username = raw_input('User name: ')
pin = raw_input('Pin code: ')
if [username,pin] in datebase:
    print "ok"