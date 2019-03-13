#题目：将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。
a = int(input('请输入正整数：'))
while a:
    for b in range(2,a):
        if a % b == 0:
            i = 1
            print(a,'= ',end='')
            while i < a:
                i += 1
                if a % i == 0 and a != i:
                    a = a / i
                    print(i,'* ',end='')
                    i -= 1
                elif a == i:
                    print(i)
            break
    else:
        print(a,'=',a,'*',1)

    a = int(input('请输入正整数：'))


