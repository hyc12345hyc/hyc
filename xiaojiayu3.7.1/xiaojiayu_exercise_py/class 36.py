# 036类和对象：给大家介绍对象
#0 定义一个Person类
class Person:
    name = "turtle"
    def print_name(self):
        print(self.name)
a = Person()
a.print_name()

#定义一个矩形类
class Rect:
    length = 5
    width = 4
    def set_rect(self):
        self.length = int(input('请输入矩形长度：'))
        self.width = int(input('请输入矩形宽度：'))
    def get_rect(self):
        print('矩形长度是%d米，宽度是%d米'%(self.length,self.width))
    def get_area(self):
        area = self.length * self.width
        print('矩形的面积是%d'% area )
old = Rect()
old.get_rect()
old.get_area()

new = Rect()
new.set_rect()
new.get_rect()
new.get_area()

