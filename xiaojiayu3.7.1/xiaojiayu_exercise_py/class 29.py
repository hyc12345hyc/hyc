# 029文件：一个任务
#将record分割成几部分
def save_file(boy,girl,count):
    boy_name = 'boy' + str(count) + '.txt'
    girl_name = 'girl' + str(count) + '.txt'
    boy_file = open(boy_name, 'w')
    girl_file = open(girl_name, 'w')
    boy_file.writelines(boy)
    girl_file.writelines(girl)
    boy_file.close()
    girl_file.close()


f = open('record.txt')
boy = []
girl = []
count = 1
for each_line in f:
    if each_line[:5] != '=====':
        (role,talking) = each_line.split(':',1)
        if role == '小甲鱼':
            boy.append(talking)
        if role == '小客服':
            girl.append(talking)
    else:
        save_file(boy, girl, count)
        boy = []
        girl = []
        count += 1
save_file(boy,girl,count)
f.close()


