import random
secret = random.randint(1,100)
# 随机数范围是1小于等于secret小于等于100
n = 0
guess = int(input("Guess the right number:(1~100)"))
while (guess != secret) and (n < 4):
    n = n + 1
    chances = str(5 - n)
    if n < 6:
        guess = int(input("Try again,only " + chances + " chances left"))
        if guess > secret:
            print ("That's too big")
        elif guess < secret:
            print ("That's too small")
        else:
            print ("BINGO,WELL DONE")
    else:
        guess = int(input("Try again,only " + chances + " chance left"))
        if guess > secret:
            print ("That's too big")
        elif guess < secret:
            print ("That's too small")
        else:
            print ("BINGO,WELL DONE")
print ("DONE")

