while 1:
    H_W = input().split()
    H = int(H_W[0])
    W = int(H_W[1])
    if H == 0:
        break
    P = {}
    i = 0
    while i < H:
        r = input()
        j = 0
        for ch in r:
            P[ch] = (i, j)
            j += 1
        i += 1
    S = input()
    ans = len(S)
    px = 0
    py = 0
    for c in S:
        x = P[c][0]
        y = P[c][1]
        if px > x:
            ans += px - x
        else:
            ans += x - px
        if py > y:
            ans += py - y
        else:
            ans += y - py
        px = x
        py = y
    print(ans)