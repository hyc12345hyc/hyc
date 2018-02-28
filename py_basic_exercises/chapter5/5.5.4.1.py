names = ['a','b','c','d']
ages = ['11','22','33','44']
for i in range(len(names)):
    print names[i],'is',ages[i],'years old'

print zip(names,ages)
for name,age in zip(names,ages):
    print name,'is',age,'years old'