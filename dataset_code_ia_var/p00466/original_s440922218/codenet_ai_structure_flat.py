while 1:
    s = input()
    if s == 0:
        break
    i = 0
    while i < 9:
        s -= input()
        i += 1
    print s