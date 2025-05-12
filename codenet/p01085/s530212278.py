while True:
    m, minn, maxn = map(int, input().split())
    if m == minn == maxn == 0:
        break
    P = [int(input()) for i in range(m)]
    ansd = 0
    ansi = 0
    for i in range(minn-1, maxn):
        if P[i] - P[i+1] >= ansd:
            ansd = P[i] - P[i+1]
            ansi = i+1
    print(ansi)