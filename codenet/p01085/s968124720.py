while True:
    m, nMin, nMax = map(int, input().split())
    if m == 0 and nMax == 0 and nMin == 0:
        break
    P = []
    Max = 0
    ans = 0
    for i in range(m):
        P.append(int(input()))
    else:
        for i in range(nMax-nMin+1):
            if i == 0 or Max <= P[nMin+i-1] - P[nMin+i]:
                Max = P[nMin+i-1] - P[nMin+i]
                ans = nMin + i
        else:
            print(ans)