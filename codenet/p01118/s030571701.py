while 1:
    H, W = map(int, input().split())
    if H == 0:
        break
    P = {}
    for i in range(H):
        r = input()
        for j, c in enumerate(r):
            P[c] = (i, j)
    S = input()
    ans = len(S)
    px = 0; py = 0
    for c in S:
        x, y = P[c]
        ans += abs(x - px) + abs(y - py)
        px = x; py = y
    print(ans)