#改进猜数字游戏，只要用户输入非整形数字，弹出输错啦，然后返回重新输入
import random
secret = random.randint(1,10)
# 随机数范围是1小于等于secret小于等于100

def right_or_wrong(guess_number):
    if guess_number > secret and n == 5:
        print("大啦，没机会啦")
    elif guess_number > secret:
        print("大啦,还有%d次机会" % (5 - n))
    elif guess_number < secret and n == 5:
        print("小啦，没机会啦")
    elif guess_number < secret:
        print("小啦,还有%d次机会" % (5 - n))
    elif guess_number == secret:
        print("猜对了，好腻害")
    elif n == 5:
        print('没机会啦，游戏结束')

temp = input("猜数字:(1~10),只有5次机会哦")
guess = int(temp)
n = 1
right_or_wrong(guess)
while (guess != secret) and (n < 5):
    temp = input("再猜一次吧:(1~100)")
    guess = int(temp)
    n = n + 1
    right_or_wrong(guess)
print ("游戏结束")
