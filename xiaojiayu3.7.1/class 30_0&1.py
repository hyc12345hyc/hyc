#0 编写一个程序，统计某目录下每种文件类型的文件数。
import os
all_files = os.listdir(r'C:\Users\Administrator\Desktop\1')                      #这里没有改变工作目录，所以路径会非常长
files_type = dict()
for each_file in all_files:
    if os.path.isdir('C:\\Users\\Administrator\\Desktop\\1\\%s' % each_file):   #这里没有改变工作目录，所以路径会非常长
        files_type.setdefault('文件夹',0)
        files_type['文件夹'] += 1
    else:
        ext = os.path.splitext(each_file)[1]
        files_type.setdefault(ext, 0)
        files_type[ext] += 1
for each_type in files_type.keys():
    print('共有(%s)类型的文件%d个' % (each_type,files_type[each_type]))

#1 编写一个程序，计算当前文件夹下所有文件的大小
import os
os.chdir(r'C:\Users\Administrator\Desktop\1')               #先改变工作目录，后续路径十分简洁
all_files = os.listdir(os.curdir)
files_dict = dict()
for each_file in all_files:
    if os.path.isfile(each_file):
        file_size = os.path.getsize(each_file)
        files_dict.setdefault(each_file,file_size)                #也可以写成files_dict[each_file] = file_size
for (key,value) in files_dict.items():                           #字典items() 函数以列表返回可遍历的(键, 值) 元组数组
    print(key,value)

