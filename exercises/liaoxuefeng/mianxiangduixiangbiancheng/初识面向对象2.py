# -*- coding:utf-8 -*-
class Person:  # 定义一个人类
    role = 'person'  # 人的角色属性都是人

    def __init__(self, name):
        self.name = name  # 每一个角色都有自己的昵称;

    def walk(self):  # 人都可以走路，也就是有一个走路方法
        print("person is walking...")


print Person.role  # 查看人的role属性
print Person.walk  # 引用人的走路方法，注意，这里不是在调用

egg = Person('egon')  #类名()就等于在执行Person.__init__()
#执行完__init__()就会返回一个对象。这个对象类似一个字典，存着属于这个人本身的一些属性和方法。

print egg.name     #查看属性直接 对象名.属性名
egg.walk()   #调用方法，对象名.方法名()