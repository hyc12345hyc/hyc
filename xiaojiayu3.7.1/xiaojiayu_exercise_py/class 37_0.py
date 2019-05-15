# 037类和对象：面向对象编程

# 0. 按照以下要求定义一个游乐园门票的类，并尝试计算2个成人+1个小孩平日票价。
# 平日票价100元 /周末票价为平日的120% /儿童半票
class Ticket:
    def __init__(self, weekend=False, child=False):
        self.price = 100
        if weekend:
            self.ratio_day = 1.2
        else:
            self.ratio_day = 1
        if child:
            self.ratio_person = 0.5
        else:
            self.ratio_person = 1
    def ticket_price(self,num):
          return self.price * self.ratio_day * self.ratio_person * num

adult = Ticket()
child = Ticket(child = True)
print("2个成人 + 1个小孩平日票价为：%.2f" % (adult.ticket_price(2) + child.ticket_price(1)))