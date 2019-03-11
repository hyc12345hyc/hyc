#计算正整数的最大约数

#如果将else语句与循环语句（while 和 for语句）进行搭配，那么只有在循环正常执行完成后才会执行else语句块的内容
def calc_max_factor(num):
    count = num // 2
    while count >  1:
        if num % count == 0:
            print('正整数%d的最大约数是%d' % (num,count))
            break
        count -= 1
    else:
        print('正整数%d是素数' % num)

num = int(input('请输入正整数：'))

calc_max_factor(num)