# -*- coding:utf:8 -*-
from math import sqrt
for n in range(99,0,-1):
    root = sqrt(n)
    if root == int(root):
        print n
        break#输出一个值就结束

while True:
    word = raw_input('Please enter a word:' )
    if not word :
        break
    print 'word','is',word

for n in range(99,81,-1):
    root = sqrt(n)
    if root == int(root):
        print n
        break
else:
        print'didn;t find a number'

