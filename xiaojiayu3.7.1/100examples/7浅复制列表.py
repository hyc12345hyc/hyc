# 题目：将一个列表的数据复制到另一个列表中。

#以下均为浅复制，原列表变化，新列表父层不变，子层会变
# 使用列表[:]
a = [1,2,3,4,5,[111,222]]
b= a[:]
print(b)

#使用for循环+列表append方法
c=[]
for i in range(len(a)):
    c.append(a[i])
print(c)

#使用列表推导式
d = [i for i in a ]
print(d)

#使用copy方法
e = a.copy()
print(e)
print('-----------')

a.append(7)
a[0] = 11
a[5][0] = 11111
print(b,c,d,e)#浅复制，原列表修改，只有列表中的列表会变