#0下面程序会输出什么：
#python可以向前引用
def next():
    print('the first one')
    pre()
def pre():
    print('the secend one')
next()
print('-----')

#1判断传入的字符串参数是否是回文联

def huiwen(sen):
    for i in range(len(sen) // 2):
        if sen[i] == sen[-i - 1]:
            x = 0
        else:
            x = 1
    if x == 0:
        return('yes')
    else:
        return('no')

print(huiwen('上海自来水来自海上'))
print('-----')

#2编写一个函数，分别统计出传入字符串参数(可能不止一个参数)的英文字母、空格、数字和其他字符的个数
def count(*para):
    for i in range(len(para)):
        letters = 0
        spaces = 0
        digits = 0
        others = 0
        for j in para[i]:
            if j.isalpha():
                letters += 1
            elif j.isdigit():
                digits += 1
            elif j == ' ':
                spaces += 1
            else:
                others += 1
        print('第%d个字符串有英文字母%d、空格%d、数字%d和其他字符%d'%(i+1,letters,spaces,digits,others))

count('csc231  ac','cas  ccccc233 qccef34 5ccc')




