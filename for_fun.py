#-*- coding:utf:8-*-
#列表反转
def reverse(li):
    for i in range(0, len(li)/2):
        temp = li[i]
        li[i] = li[-i-1]
        li[-i-1] = temp

l = [1, 2, 3, 4, 5]
reverse(l)
print(l)


def triple(*nums):
    s = 0
    for n in nums:
        s = s + n * n * n
    print s
    return s
triple(*[3,4])
