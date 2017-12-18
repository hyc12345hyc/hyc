#-*- coding:utf-8 -*
number = 23
running = True
while running:
    guess = int(input('guess:'))

    if guess == number:
        print('great')
        # 这将导致 while 循环中止
        running = False
    elif guess > number:
        print('too big')
    else:
        print('too small')
else:
    print('The while loop is over.')
    # 在这里你可以做你想做的任何事
print('done')