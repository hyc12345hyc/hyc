#0 定义一个Person类
class Person:
    name = "turtle"
    def printname(self):
        print(self.name)

Person().printname()

#定义一个矩形类
class Rect:
    length = 5
    width = 4
    def setRect(self):
        self.length = int(input('请输入矩形长度：'))
        self.width =  int(input('请输入矩形宽度：'))
    def getRect(self):
        print('矩形长度是%d米，宽度是%d米'%(self.length,self.width))
    def getArea(self):
        area = self.length * self.width
        print('矩形的面积是%d'%(area))

