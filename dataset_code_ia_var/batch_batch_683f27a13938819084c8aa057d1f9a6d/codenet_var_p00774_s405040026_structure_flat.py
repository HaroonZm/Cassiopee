while 1:
    n = int(input())
    if n == 0:
        break
    f = [list(map(int, input().split())) for _ in range(n)]
    d = True
    ans = 0
    while d:
        d = False
        i = 0
        while i < n:
            l = []
            k = 0
            while k < 3:
                if f[i][k] == 0:
                    k += 1
                    continue
                if f[i][k] == f[i][k + 1] == f[i][k + 2]:
                    l.append(k)
                    l.append(k + 1)
                    l.append(k + 2)
                k += 1
            if l == []:
                i += 1
                continue
            l2 = []
            for x in l:
                if x not in l2:
                    l2.append(x)
            l = l2
            b = f[i][l[0]]
            d = True
            for k in l:
                ans += b
                f[i][k] = 0
            i += 1
        if d:
            i = n - 1
            while i >= 0:
                k = 0
                while k < 5:
                    x = i
                    while f[x][k]:
                        if x < n - 1:
                            if f[x + 1][k] == 0:
                                f[x + 1][k] = f[x][k]
                                f[x][k] = 0
                                x += 1
                                continue
                        break
                    k += 1
                i -= 1
    print(ans)