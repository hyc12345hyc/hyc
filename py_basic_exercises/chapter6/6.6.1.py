n = input('enter in integer:')

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

def factorial_1(n):
    result = n
    for i in range (1,n):
        result = result * i
    return result


print factorial(n)
print factorial_1(n)