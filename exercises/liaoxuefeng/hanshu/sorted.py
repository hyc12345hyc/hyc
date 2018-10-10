#-*- coding:utf-8 -*-
# 比较字符串大小（无视大小写）

def f(str1,str2):
    x = str1.lower()    #  x = str.upper()    OK
    y = str2.lower()
    if x > y:
        return 1
    if x < y:
        return -1
    else:              #  return 0    OK
        return 0

print sorted(['ZZ','a','bb','CC'],f)



print sorted([36, 5, 12, 9, 21])



