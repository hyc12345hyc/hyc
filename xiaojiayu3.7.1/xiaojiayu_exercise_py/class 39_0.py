# 039类和对象：拾遗
# 0. 思考这一讲我学习的内容，请动手在一个类中定义一个变量，用于跟踪该类有多少个实例被创建（当实例化一个对象，这个变量+1，当销毁一个对象，这个变量自动-1）
class A:
    count = 0
    def __init__(self):
        A.count += 1
    def __del__(self):
        A.count -= 1

a = A()
b = A()
c = A()
print(A.count)

del b
print(A.count)

