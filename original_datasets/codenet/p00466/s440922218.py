while 1:
    s = input()
    if s == 0: break
    for i in range(9): s -= input()
    print s