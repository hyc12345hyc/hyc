#编写一个程序，用户输入文件名以及开始搜索的路径，搜索该文件是否存在。如遇到文件夹，则进入文件夹继续搜索。
import os
index = input('请输入开始搜索的路径:')
target = input('请输入目标文件:')

def search_file(index,target):
    os.chdir(index)
    for each_file in os.listdir(os.curdir):
        if each_file == target:
            print(os.getcwd() + os.sep + each_file)         #使用os.sep使程序更标准
        if os.path.isdir(each_file):
            search_file(each_file,target)                   #递归调用
            os.chdir(os.pardir)                             #递归调用后切记返回上一层目录


search_file(index,target)
#C:\Users\Administrator\Desktop\1


