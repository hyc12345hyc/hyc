#input()函数有可能产生两类异常：EOFError（文件末尾endoffile，当用户按下组合件Ctrl+d产生）
# 和KeyboardInterrupt（取消输入，当用户按下组合键Ctrl+c产生）
#捕获处理input()的两类异常，提高用户体验

import random
secret = random.randint(1,10)
try:
    temp = input("猜数字:(1~10),只有5次机会哦")
    guess = int(temp)
except (ValueError,EOFError,KeyboardInterrupt):
    print('输入错误！')
    guess = secret
while (guess != secret):
    temp = input("再猜一次吧:(1~10)")
    guess = int(temp)
    if guess == secret:
        print("猜对了，好腻害")
    else:
        if guess > secret:
            print("大啦")
        else:
            print("小啦")
print ("游戏结束")


