while True:
    n = int(input())
    if n == 0:
        break
    f = [0,0,0,0,0,0,0,0,0,0]
    i = 0
    while i < n:
        x = int(input())
        f[x] = f[x] + 1
        i = i + 1
    i = 0
    while i < 10:
        if f[i] == 0:
            print('-')
        else:
            print('*' * f[i])
        i = i + 1