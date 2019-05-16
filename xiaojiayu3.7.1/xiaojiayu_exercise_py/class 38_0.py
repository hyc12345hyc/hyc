'''
多重继承使用不当会导致重复调用（也叫钻石继承、菱形继承）的问题，请分析以下代码在实际编程中有可能导致什么问题？

答：多重继承容易导致重复调用问题，下边实例化 D 类后我们发现 A 被前后进入了两次。
这有什么危害？我举个例子，假设 A 的初始化方法里有一个计数器，那这样 D 一实例化，A 的计数器就跑两次（如果遭遇多个钻石结构重叠还要更多），
很明显是不符合程序设计的初衷的（程序应该可控，而不能受到继承关系影响）。
'''
class A:
    def __init__(self):
        print("进入A…")
        print("离开A…")

class B(A):
    def __init__(self):
        print("进入B…")
        A.__init__(self)
        print("离开B…")

class C(A):
    def __init__(self):
        print("进入C…")
        A.__init__(self)
        print("离开C…")

class D(B, C):
    def __init__(self):
        print("进入D…")
        B.__init__(self)
        C.__init__(self)
        print("离开D…")

d = D()

print('————————————')

'''
如何解决上一题中出现的问题？
答：super 函数再次大显神威。
'''


class E():
    def __init__(self):
        print("进入A…")
        print("离开A…")


class F(E):
    def __init__(self):
        print("进入B…")
        super().__init__()
        print("离开B…")


class G(E):
    def __init__(self):
        print("进入C…")
        super().__init__()
        print("离开C…")


class H(F, G):
    def __init__(self):
        print("进入D…")
        super().__init__()
        print("离开D…")

h = H()