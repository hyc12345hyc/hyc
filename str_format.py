#-*- coding:utf-8 -*
name = 'miracle'
age = 19
print("{0} is {1} years old ".format(name, age))
print('Why is {0} playing with that python?'.format(name))
#一个字符串可以使用某些特定的格式（Specification）， 随后， format  方法将被调用，使用这一方法中与之相应的参数替换这些格式。
# 在这里要注意我们第一次应用这一方法的地方，此处  {0}  对应的是变量  name  ，它是该格式化方法中的第一个参数。
# 与之类似，第二个格式  {1}  对应的是变量  age  ，它是格式化方法中的第二个参数。
# 请注意，Python 从 0 开始计数，这意味着索引中的第一位是 0，第二位是1，以此类推。

# 对于浮点数 '0.333' 保留小数点(.)后三位
#.3 指定除小数点外的输出位数;.3f 表示浮点数的精度为3（小数位保留3位）
print('{0:.3f}'.format(1.0/3))
# 使用下划线填充文本，并保持文字处于中间位置
# 使用 (^) 定义 '___hello___'字符串长度为 11
print('{0:_^11}'.format('hello'))
# 基于关键词输出 'Swaroop wrote A Byte of Python'
print('{name} wrote {book}'.format(name='Swaroop', book='A Byte of Python'))

print('\"What\'s your {0} ?\"\n\"How {1} are you ?\"'.format('name','old'))

print(r'"Newlines are indicated by \n"')
