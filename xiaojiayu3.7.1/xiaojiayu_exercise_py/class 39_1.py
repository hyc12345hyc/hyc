#1. 定义一个栈（Stack）类，用于模拟一种具有后进先出（LIFO）特性的数据结构。至少需要有以下方法：
# 方法名	                     含义
# isEmpty()	                 判断当前栈是否为空（返回 True 或 False）
# push()	                 往栈的顶部压入一个数据项
# pop()	                     从栈顶弹出一个数据项（并在栈中删除）
# top()	                     显示当前栈顶的一个数据项
# bottom()	                 显示当前栈底的一个数据项

class Stack1:
    def __init__(self, ini = []):
        self. stack = []
        for x in ini:
            self.push(x)

    def isEmpty(self):
        print(not self.stack)

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        if not self.stack:
            print('警告，栈为空！')
        else:
            self.stack.pop()

    def top(self):
        if not self.stack:
            print('警告，栈为空！')
        else:
            print(self.stack[-1])

    def bottom(self):
        if not self.stack:
            print('警告，栈为空！')
        else:
            print(self.stack[0])

    def printAll(self):
        print(self.stack)



a = Stack1([2,3,4,5])
a.isEmpty()
a.push('new1')
a.push('new2')
a.printAll()
a.top()
a.bottom()
a.pop()
a.printAll()


