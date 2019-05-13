x = '{0:.2f}{1}'.format(2222.2222,'GB')
print(x)

y = '{a}{b}'.format(a = 'he',b = 'llo')
print(y)

z = '%c' % 97
print(z)
zz = '%c %c' % (98,99)
print(zz)

print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)

print('成绩提升了 %30.20f %%' % ((82-75)/75))

print('Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125))


print("{{1}}".format("不打印", "打印"))

print('{0}{1:.2f}'.format('Pi = ', 3.1415))