while 1:
    n = int(raw_input())
    if n == 0:
        break
    c = 0
    while n != 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = n * 3 + 1
        c = c + 1
    print c