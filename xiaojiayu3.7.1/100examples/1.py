#题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
count = 0
list = []
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if i != j and j != k and k != i:
                count += 1
                answer = (i*100 + j*10 + k)
                list.append(answer)
print('符合条件的数字共有%d个，分别是:\n'% count , list)


