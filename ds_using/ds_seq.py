#-*- coding:utf-*-
shoplist = ['apple','mango','carrot','banana']
name = 'swaroop'

# Indexing or 'Subscription' operation #
# 索引或“下标（Subscription）”操作符 #
#Python 从 0 开始计数。因此  shoplist[0]将获得  shoplist  序列中的第一个项目，而  shoplist[3]  将获得第四个项目。
#索引操作也可以使用负数，在这种情况下，位置计数将从队列的末尾开始。
# 因此， shoplist[-1]  指的是序列的最后一个项目， shoplist[-2]  将获取序列中倒数第二个项目。

print 'Item 0 is',shoplist[0]
print 'Item 1 is',shoplist[1]
print 'Item 2 is',shoplist[2]
print 'Item 3 is',shoplist[3]
print 'Item -1 is',shoplist[-1]
print 'Item -2 is',shoplist[-2]
print 'Character 0 is',name[0]

# Slicing on a list #
#在切片操作中，第一个数字（冒号前面的那位）指的是切片开始的位置，第二个数字（冒号后面的那位）指的是切片结束的位置。
# 如果第一位数字没有指定，Python 将会从序列的起始处开始操作。如果第二个数字留空，Python 将会在序列的末尾结束操作。

print 'Item 1 to 3 is',shoplist[1:3]
print 'Item 1 to end is',shoplist[1:]
print 'Item 1 to -1 is',shoplist[1:-1]
print 'Item start to end is',shoplist[:]

# 从某一字符串中切片 #

print 'Characters 1 to 3 is',name[1:3]
print 'Characters 1 to end is',name[1:]
print 'Characters 1 to -1 is',name[1:-1]
print 'Characters start to end is',name[:]
print 'Charcater start to -1 is',name[:-1]

#同样可以在切片操作中提供第三个参数，这一参数将被视为切片的步长（Step）（在默认情况下，步长大小为 1）。

print shoplist[::1]
print shoplist[::2]
print shoplist[::3]
print shoplist[::-1]