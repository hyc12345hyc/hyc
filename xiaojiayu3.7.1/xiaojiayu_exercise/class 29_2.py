#编写一个程序，接受用户的输入并保存为新的文件
file_name = input('请输入文件名:')
f = open(file_name + '.txt','w')
while True:
    file_text = input('请输入正文:(单独输入":w"保存退出):')
    if file_text != ':w':
        f.write(file_text)
    else:
        break
f.close()

