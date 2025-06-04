def trans(x):
    res = ''
    def go(y):
        return str(y%4) if not int(y/4) else go(int(y/4)) + str(y%4)
    return go(x)
run = True
while run:
    t = input()
    if t == '-1':
        run = False
    else:
        n4 = (lambda val: trans(int(val)))(t)
        print(n4)