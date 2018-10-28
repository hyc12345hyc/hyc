# 尝试利用字典的特性编写一个通讯录程序

print('|--- 欢迎进入通讯录程序 ---|')
print('|--- 1：查询联系人资料  ---|')
print('|--- 2：插入新的联系人  ---|')
print('|--- 3：删除已有联系人  ---|')
print('|--- 4：显示当前通讯录  ---|')
print('|--- 5：退出通讯录程序  ---|')

dict1 = {'xiaoming': 123456}
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
            print(name + '此人已存在')
            print(name + str(dict1[name]))
            if input('是否要修改 %s 此人电话？(YES/NO)'%name) == 'YES':
                dict1[name] = input('请输入新电话号码：')
        else:
            dict1[name] = int(input('请输入电话号码：'))
            print('已添加%s %s'%(name,str(dict1[name])))
    if number == 3:
        name = input(('请输入姓名：'))
        if name in dict1:
            if input('是否要删除%s此人信息？(YES/NO)'%name) == 'YES':
                del (dict1[name])
        else:
            print('查无此人')
    if number == 4:
        print(dict1)
    if number == 5:
        break