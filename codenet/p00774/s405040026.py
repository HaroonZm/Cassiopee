def main(n):
    f = [list(map(int, input().split())) for i in range(n)]
    d = True
    ans = 0
    while d:
        d = False
        for i in range(n):
            l = []
            for k in range(3):
                if f[i][k] == 0:
                    continue
                if f[i][k] == f[i][k + 1] == f[i][k + 2]:
                    l.append(k)
                    l.append(k + 1)
                    l.append(k + 2)
            if l == []:
                continue
            l = list(set(l))
            b = f[i][l[0]]
            d = True
            for k in l:
                ans += b
                f[i][k] = 0
        if d:
            for i in range(n-1,-1,-1):
                for k in range(5):
                    x = i
                    while f[x][k]:
                        if x < n - 1:
                            if f[x + 1][k] == 0:
                                f[x+1][k] = f[x][k]
                                f[x][k] = 0
                                x += 1
                                continue
                        break
    print(ans)

while 1:
    n = int(input())
    if n == 0:
        break
    main(n)