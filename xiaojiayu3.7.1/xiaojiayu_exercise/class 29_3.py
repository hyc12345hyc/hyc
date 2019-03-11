#实现全部替换功能
def file_replace(file_name,rep_word,new_word):
    f_read = open(file_name)

    content = []
    count = 0

    for each_line in f_read:
        if rep_word in each_line:
            count = each_line.count(rep_word)
            each_line = each_line.replace(rep_word,new_word)
        content.append(each_line)

    decide = input('\n文件%s中共有%s个%s\n您确定要把所有的%s替换为%s吗？\n(yes/no)'\
        % (file_name,count,rep_word,rep_word,new_word))

    if decide in ['YES','Yes','yes']:
        f_write = open(file_name,'w')
        f_write.writelines(content)
        f_write.close()

file_name = input('请输入文件名:')
rep_word = input('请输入需替换的单词或字符:')
new_word = input('请输入新的单词或字符:')
file_replace(file_name,rep_word,new_word)