#创建字典的各种方法
dict1 = dict((['one',1],['two',2],['three',3]))
dict2 = dict([('one',1),('two',2),('three',3)])
dict3 = dict(one=1,two=2,three=3)
dict4 = {'one':1,'two':2,'three':3}
dict5 = dict(zip(['one','two','three'],[1,2,3]))
print(dict1)
print(dict2)
print(dict3)
print(dict4)
print(dict5)
print(type(dict1))
print('---------')

notadict = {'one:1','two:2','three:3'}
print(type(notadict))

#尝试利用字典的特性编写一个通讯录程序

print('|--- 欢迎进入通讯录程序 ---|')
print('|--- 1：查询联系人资料  ---|')
print('|--- 2：插入新的联系人  ---|')
print('|--- 3：删除已有联系人  ---|')
print('|--- 4：退出通讯录程序  ---|')

dict1 = {'xiaoming':123456}
while True:
    number = int(input('请输入指令数字：'))
    if number == 1:
        name = input(('请输入姓名：'))
        if name in dict1:
            print(name + str(dict1[name]))
        else:
            print('查无此人')

    if number == 2:
        name = input(('请输入姓名：'))
        if name in dict1:
            print('此人已存在')
            print(name + str(dict1[name]))
            if input('是否要修改此人电话？(YES/NO)') == 'YES':
                dict1[name] = input('请输入新电话号码：')
        else:
            dict1[name] = int(input('请输入电话号码：'))
            print('已添加'+ name + ':' + str(dict1[name]))
    if number == 3:
        name = input(('请输入姓名：'))
        if name in dict1:
            if input('是否要删除此人信息？(YES/NO)') == 'YES':
                del(dict1[name])
        else:
            print('查无此人')

    if number == 4:
        break

    if number == 5:
        print(dict1)