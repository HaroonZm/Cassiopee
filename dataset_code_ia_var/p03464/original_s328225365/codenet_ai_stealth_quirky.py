def _():
    import sys as S
    k = int(S.stdin.readline())
    a = [int(x) for x in S.stdin.readline().split()]
    if a[-1]^2:
        S.stdout.write('-1\n')
        S.exit()

    X, Y = 2, 2
    i = k
    while i:
        i -= 1
        t = a[i]
        X = (-(-X//t))*t
        Y = (Y//t)*t + (t-1)
        if Y < X:
            print(~0)
            return
    print(X, Y)
_()