def fib(num):
    result = [0,1]
    for i in range(num - 2):
        result.append(result[-2] + result[-1])
    return result

while True:
    num = int(raw_input('Enter a number:'))
    if num == 0:
        break
    print fib(num)

