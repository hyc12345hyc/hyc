# 使用递归求解以下问题。
# 5个人坐在一起，第五个人比第四个人大2岁，第四个人比第三个人大2岁，以此类推，第一个人10岁，求第五个人几岁。
def age(n):
    if n == 1:
        return 10
    else:
        return age(n-1) + 2
print('第五个人的年龄是%d岁' % age(5))

#写一个函数get_digits(n)，将参数n分解出每位的数字并按顺序存放到列表中。举例：get_digits(12345) ---> [1,2,3,4,5]
result = []
def get_digits(n):
    if n > 1:
        result.insert(0,n%10)
        get_digits(n//10)
get_digits(23123)
print(result)
