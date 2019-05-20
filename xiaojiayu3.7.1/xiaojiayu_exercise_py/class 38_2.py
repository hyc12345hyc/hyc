# 0. 定义一个点（Point）类和直线（Line）类，使用 getLen 方法可以获得直线的长度。
# 提示：
# 1.设点 A(X1,Y1)、点 B(X2,Y2)，则两点构成的直线长度 |AB| = √((x1-x2)2+(y1-y2)2)
# 2.Python 中计算开根号可使用 math 模块中的 sqrt 函数
# 3.直线需有两点构成，因此初始化时需有两个点（Point）对象作为参数

import math
class Point:
    def __init__(self):
        self.x = int(input('enter p_x'))
        self.y = int(input('enter p_y'))
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y


class Line:
    def __init__(self, p1, p2):
        self.x1 = p1.get_x()
        self.y1 = p1.get_y()
        self.x2 = p2.get_x()
        self.y2 = p2.get_y()
        self.len = math.sqrt((self.x1 - self.x2) ** 2 + (self.y1 - self.y2) ** 2)
    def get_len(self):
        return self.len

p_1 = Point()
p_2 = Point()
length = Line(p_1, p_2)
print(length.get_len())
