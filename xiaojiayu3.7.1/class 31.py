import pickle
my_list = [1,3,'aaa',['bbbb']]
pickle_file = open('pickle_my_list.pkl','wb')
pickle.dump(my_list , pickle_file)
pickle_file.close()

pickle_file = open('pickle_my_list.pkl','rb')
my_list2 = pickle.load(pickle_file)
print(my_list2)


#编写一个程序，要求使用pickle分割文件(record.txt)
import pickle
def save_file(boy,girl,count):
    boy_name = 'boy' + str(count) + '.txt'
    girl_name = 'girl' + str(count) + '.txt'
    boy_file = open(boy_name, 'wb')
    girl_file = open(girl_name, 'wb')
    pickle.dump(boy, boy_file)
    pickle.dump(girl, girl_file)
    boy_file.close()
    girl_file.close()

def split_file(file_name):
    count = 1
    boy = []
    girl = []
    f = open(file_name)

    for each_line in f:
        if each_line[:6] != '======':
            (role,line_spoken) = each_line.split(':' , 1)
            if role == '小甲鱼':
                boy.append(line_spoken)
            if role == '小客服':
                girl.append(line_spoken)

        else:
            save_file(boy,girl,count)

            boy = []
            girl = []
            count += 1

    save_file(boy,girl,count)#第三段之后没有'=====',手动执行一次保存操作
    f.close()

split_file('record.txt')
