#-*- coding:utf -*-
x=[]
for m in range(-84,84):
    for n in range(-84,84):
        if (m+n)*(m-n)==168:#m,n都是整数
            x.append(n**2-100)
print x
x=set(x)#用集合的方法去掉重复值
print x
x=list(x)#将集合类型改为列表类型
print'要求的值为：',x