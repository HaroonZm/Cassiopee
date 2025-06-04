while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    step = 0
    if n >= m:
        X = n
        Y = m
    else:
        X = m
        Y = n
    while True:
        X = X % Y
        X, Y = Y, X
        step += 1
        if Y == 0:
            ans = X
            break
    print(ans, step)