#编写一个程序，用户输入开始搜索的路径，查找该路径下(包含子文件夹内)所有的文本格式文件(txt,doc和docx)
#并创建一个文件(txtlist.txt)存放所有找到的文件的路径。

import os
index = input('请输入开始搜索的路径:')
target = ['.txt','.doc','.docx']
txt_list = []

def search_file(index,target):
    os.chdir(index)

    for each_file in os.listdir(os.curdir):
        ext = os.path.splitext(each_file)[1]
        if ext in target:
            txt_list.append(os.getcwd() + os.sep + each_file + os.linesep)        #使用os.sep使程序更标准
        if os.path.isdir(each_file):
            search_file(each_file,target)                                           #递归调用
            os.chdir(os.pardir)                                                     #递归调用后切记返回上一层目录

program_dir = os.getcwd()

search_file(index,target)

f = open(index + os.sep + 'txtlist.txt','w')
f.writelines(txt_list)
f.close()


