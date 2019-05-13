#尝试一个新函数int_input()当用户输入整数时正常返回，否则提示出错并要求重新输入
def int_input():
    while True:
        try:
            print(int(input()))
            break
        except ValueError:
            print('错啦，重新输入')

int_input('请输入整数:')