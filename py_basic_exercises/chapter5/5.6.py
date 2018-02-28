a = [x*x for x in range(10)]
print a
b = [x*x for x in range(10) if x % 3 == 0]
print b
c = [(a,b) for a in range(3) for b in range(3)]
print c