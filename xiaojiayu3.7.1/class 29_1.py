#编写一个程序，当用户输入文件名和行数(N)后，将该文件的前(N)行内容打印到屏幕上。
f = open('record.txt')
n = input('请输入行数：')
for i in range(int(n)):
    print(f.readline())
f.close()

#扩展一下，用户可以随意输入需要显示的行数。（如13:21打印13-21行，:21打印前21行，21:打印第21行到最后）
def file_view(file_name,line_num):
    if line_num.strip() == ':':#去除引号首尾的空格
        begin = '1'
        end = '-1'

    (begin,end) = line_num.split(':')

    if begin == '':
        begin = '1'
    if end == '':
        end = '-1'

    if begin == '1' and end == '-1':
        prompt = '的全文'
    elif begin == '1':
        prompt = '从开始到%s' % end
    elif end == '-1':
        prompt = '从%s到结束' % begin
    else:
        prompt = '从第%s到第%s行' % (begin,end)

    print('\n文件%s%s的内容如下:\n' % (file_name,prompt))

    begin = int(begin) - 1
    end = int(end)
    lines = end - begin

    f = open(file_name)

    for i in range(begin):
        f.readline()           #用于消耗掉begin之前的内容

    if lines < 0:
        print(f.read())        #end为-1时lines小于零，此时打印全文
    else:
        for j in range(lines):
            print(f.readline(),end = '')
    f.close()

file_name = input('请输入要打开的文件：')
line_num = input('请输入需要现实的行数：')
file_view(file_name,line_num)


