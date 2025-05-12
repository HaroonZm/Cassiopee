def main(m, nx, nn):
    b = [int(input()) for i in range(m)]
    d = -1
    for i in range(nn, nx + 1):
        if d <= b[i - 1] - b[i]:
            d = b[i - 1] - b[i]
            ans = i
    print(ans)
while 1:
    m, nmin, nmax = map(int, input().split())
    if m == nmax == nmin == 0:
        break
    main(m,nmax, nmin)