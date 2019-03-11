#编写一个程序，用户输入关键字，查找当前文件夹内(如果当前文件夹内包含文件夹，# 则进入文件夹继续搜索)
# 所有含有该关键字的文本文件(.txt后缀)，要求显示该文件所在的位置以及关键字在文件中的具体位置(第几行第几个字符)

import os
key = input('请输入关键字:')
detail = input('请问是否需要打印关键字【%s】在文件中的具体位置(yes/no):' % key)

os.chdir(r'C:\Users\Administrator\Desktop\1')               #切换到需查找的文件夹

def search_files(key , detail):                                  #查找key是否存在，detail判断是否要给出确定位置
    all_files = os.walk(os.getcwd())
    text_files = []
    #walk 方法介绍
    #walk 方法遍历当前目录,返回的是一个三元组(root, dirs, files)
    # root 所指的是当前正在遍历的这个文件夹的本身的地址
    # dirs 是一个list, 内容是该文件夹中所有的目录的名字(不包括子目录)
    # files 同样是 list, 内容是该文件夹中所有的文件(不包括子目录)
    for i in all_files:
        for each_file in i[2]:
            if os.path.splitext(each_file)[1] == '.txt':        #根据后缀判断是否是文本文件
                each_file = os.path.join(i[0],each_file)
                text_files.append(each_file)                     #列表储存所有路径中的文本文件的路径
    for each_txt_file in text_files:
        key_dict = search_in_file(each_txt_file , key)
        if key_dict:
            print('====================================================')
            print('在文件【%s】中找到关键字【%s】' % (each_txt_file , key))
            if detail in ['YES','Yes','yes']:
                print_pos(key_dict)

def search_in_file(file_name , key):
    f = open(file_name)
    count = 0                                                   #记录行数
    key_dict = dict()                                           #字典，用户存放key所在具体行数对应具体位置{行数:[位置1,位置2]}

    for each_line in f:
        count += 1
        if key in each_line:
            pos = pos_in_line(each_line , key)                  #key在每行对应的位置
            key_dict[count] = pos
    f.close()
    return key_dict

def pos_in_line(line , key):
    pos = []
    begin = line.find(key)                                      #key在line中的位置
    while begin != -1:                                         #find方法找不到时返回-1,找到的话就将一个位置存入pos列表
        pos.append(begin + 1)                                   #用户的角度是从1开始数
        begin = line.find(key , begin+1)                        #从下一个位置继续查找
    return pos

def print_pos(key_dict):
    keys = key_dict.keys()
    keys = sorted(keys)                                         #由于字典是无序的，我们这里对行数进行排序
    for each_keys in keys:
        print('关键字出现在第%s行，第%s位置' % (each_keys , str(key_dict[each_keys])))



search_files(key,detail)