answer = 666
n = 0
guess = int(input("Guess the right number:(1~999)"))
while guess != answer:
    n = n + 1
    if n > 4:
        break
    chances = str(5 - n)
    if n < 6:
        guess = int(input("Try again,only " + chances + " chances left"))
        if guess > answer:
            print ("That's too big")
        elif guess < answer:
            print ("That's too small")
        else:
            print ("BINGO,WELL DONE")
    else:
        guess = int(input("Try again,only " + chances + " chance left"))
        if guess > answer:
            print ("That's too big")
        elif guess < answer:
            print ("That's too small")
        else:
            print ("BINGO,WELL DONE")
print ("DONE")

