
while True:
    try:
        a = int(input('请输入：'))
        if a > 10 and a != 0:
            print('数据过大请重新输入：')
            a = int(input('请输入：'))
        elif a == 0:
            break
        else:
            print(a**2)
    except ValueError:
        print('数据类型错误')
        break
