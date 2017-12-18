while True:
    s = raw_input('Enter something;')
    if s == 'quit':
        break
    if len(s) < 5:
        print('too small')
        continue
    print('The data is out of range')
    