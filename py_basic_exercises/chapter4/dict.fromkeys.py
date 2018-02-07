#-*- coding:utf-8 -*-
seq = ('name', 'age', 'sex')

dict = dict.fromkeys(seq)
print "New Dictionary : %s" %  str(dict)

dict = dict.fromkeys(seq, 10)
print "New Dictionary : %s" %  str(dict)

#语法
#fromkeys()方法语法：
#dict.fromkeys(seq[, value]))
#参数
#seq -- 字典键值列表。
#value -- 可选参数, 设置键序列（seq）的值。