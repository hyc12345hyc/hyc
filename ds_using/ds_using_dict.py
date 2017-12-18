
#-*-coding:utf-*-
# “ab”是地址（Address）簿（Book）的缩写
#在字典中，你可以通过使用符号构成  d = {key : value1 , key2 : value2}  这样的形式，来成对地指定键值与值。
# 在这里要注意到成对的键值与值之间使用冒号分隔，而每一对键值与值则使用逗号进行区分，它们全都由一对花括号括起。
ab = {
    'Swaroop':'swaroop@swaroopch.com',
    'Larry':'larry@wall.org',
    'Matsumoto': 'matz@ruby-lang.org',
    'Spammer': 'spammer@hotmail.com'
}

print "Swaroop's address is",ab['Swaroop']

# 删除一对键值—值配对
del ab['Spammer']

print '\nThere are {} contacts in the address-book\n'.format(len(ab))

for name,address in ab.items():
    print 'Contact {} at {}'.format(name,address)

# 添加一对键值—值配对
ab['Guido'] = 'guido@python.org'

if 'Guido' in ab:
    print "\nGuido's address is",ab['Guido']
