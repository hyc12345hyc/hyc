#-*-coding:utf-*-

name = 'Swaroop'

if name.startswith('Swa'):
    print 'Yes,the string starts with "Swa".'
if 'a' in name:
    print 'Yes,it contains the string "a".'
if name.find('waro') != -1:
    print 'Yes,it contains the string "waro".'

delimiter = '_*_'
mylist = ['Brazil', 'China','America','Russia']
print delimiter.join(mylist)
print mylist
