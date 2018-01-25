# -*- coding:utf:8 -*-

#访问字典里的值
#把相应的键放入熟悉的方括弧，如下实例:
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print "dict['Name']: ", dict['Name']
print "dict['Age']: ", dict['Age']

#修改字典
#向字典添加新内容的方法是增加新的键/值对，修改或删除已有键/值对如下实例:
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
dict['Age'] = 8  # update existing entry
dict['School'] = "DPS School"  # Add new entry
print "dict['Age']: ", dict['Age']
print "dict['School']: ", dict['School']
print dict

#删除字典元素
#能删单一的元素也能清空字典，清空只需一项操作。
#显示删除一个字典用del命令，如下实例：
# del dict['Name'] 删除键是'Name'的条目
# dict.clear()     清空词典所有条目
# del dict         删除词典