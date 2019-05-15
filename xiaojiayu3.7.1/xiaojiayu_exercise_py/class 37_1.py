# 1. 游戏编程：按以下要求定义一个乌龟类和鱼类并尝试编写游戏。（初学者不一定可以完整实现，但请务必先自己动手，你会从中学习到很多知识的^_^）
# 假设游戏场景为范围（x, y）为0<=x<=10，0<=y<=10
# 游戏生成1只乌龟和10条鱼
# 它们的移动方向均随机
# 乌龟的最大移动能力是2（Ta可以随机选择1还是2移动），鱼儿的最大移动能力是1
# 当移动到场景边缘，自动向反方向移动
# 乌龟初始化体力为100（上限）
# 乌龟每移动一次，体力消耗1
# 当乌龟和鱼坐标重叠，乌龟吃掉鱼，乌龟体力增加20
# 鱼暂不计算体力
# 当乌龟体力值为0（挂掉）或者鱼儿的数量为0游戏结束
import random as r
#限制游戏场景范围
area_x = [0,10]
area_y = [0,10]

class Turtle:
    def __init__(self):
        #初始体力
        self.health = 100
        #初始位置随机
        self.x = r.randint(area_x[0], area_x[1])
        self.y = r.randint(area_y[0], area_y[1])
    def move(self):
        # 随机计算方向并移动到新的位置（x, y）
        new_x = self.x + r.choice([-1, -2, 1, 2])
        new_y = self.y + r.choice([-1, -2, 1, 2])
        # 检查移动后是否超出场景x轴边界
        if new_x < area_x[0]:
            self.x = -new_x
        elif new_x > area_x[1]:
            self.x = area_x[1] - (new_x - area_x[1])
        else:
            self.x = new_x
        # 检查移动后是否超出场景y轴边界
        if new_y < area_y[0]:
            self.y = -new_y
        elif new_y > area_y[1]:
            self.y = area_y[1] - (new_y - area_y[1])
        else:
            self.y = new_y
        # 体力消耗
        self.health -= 1
        # 返回移动后的新位置
        return self.x, self.y
    def eat(self):
        self.health += 20
        if self.health > 100:
            self.health = 100

class Fish:
    def __init__(self):
        self.x = r.randint(area_x[0], area_x[1])
        self.y = r.randint(area_y[0], area_y[1])
    def move(self):
        new_x = self.x + r.choice([-1, 1])
        new_y = self.y + r.choice([-1, 1])
        if new_x < area_x[0]:
            self.x = -new_x
        elif new_x > area_x[1]:
            self.x = area_x[1] - (new_x - area_x[1])
        else:
            self.x = new_x
        if new_y < area_y[0]:
            self.y = -new_y
        elif new_y > area_y[1]:
            self.y = area_y[1] - (new_y - area_y[1])
        else:
            self.y = new_y
        return self.x, self.y

turtle = Turtle()
fish = []
for i in range (10):
    new_fish = Fish()
    fish.append(new_fish)

while True:
    if not len(fish):
        print('turtle win')
        break
    elif not turtle.health:
        print('fish win')
        break

    pos = turtle.move()
    # 在迭代器中删除列表元素是非常危险的，经常会出现意想不到的问题，因为迭代器是直接引用列表的数据进行引用
    # 这里我们把列表拷贝给迭代器，然后对原列表进行删除操作就不会有问题了^_^
    for each_fish in fish[:]:
        if each_fish.move() == pos:
            # 鱼被吃了
            turtle.eat()
            fish.remove(each_fish)
            print('一条鱼被吃了')












