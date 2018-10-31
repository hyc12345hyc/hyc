#编写一个程序，用户输入关键字，查找当前文件夹内(如果当前文件夹内包含文件夹，# 则进入文件夹继续搜索)
# 所有含有该关键字的文本文件(.txt后缀)，要求显示该文件所在的位置以及关键字在文件中的具体位置(第几行第几个字符)

import os
index = input('请输入开始搜索的路径:')
keyword = input('请输入关键字:')

file_place = []                         #含有该关键字的文本文件
os.chdir(index)
def search_keyword(index,keyword):
    for each_file in os.listdir(os.curdir):
        if os.path.splitext(each_file)[1] == '.txt':
            f_read = open(each_file)
            for each_line in f_read:
                if keyword in each_line:
                    file_place.append(os.getcwd() + each_file)
            f_read.close()
    print(file_place)
search_keyword(index,keyword)