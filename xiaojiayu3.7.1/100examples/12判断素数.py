# 题目：判断101-200之间有多少个素数，并输出所有素数。
l = []
for i in range(101,200):
    for j in range(2,i-1):
        if i % j == 0:
            break#这个不能漏
    else:
        l.append(i)
print(l)
print(len(l))

#当迭代的对象迭代完并为空时，位于else的子句将执行，而如果在for循环中含有break时则直接终止循环，并不会执行else子句。
