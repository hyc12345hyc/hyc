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

data = '123,13,333'
print(data.split(','))

a = {1:1,2:2,3:[3,4]}
b = a.copy()
c = a

a[3].append(5)
print(b,c)

