INF = 100000
while True:
    n = int(input())
    if not n:
        break
    lst = []
    for _ in range(n):
        lst.append(int(input()))
    ans = INF
    for i in range(n):
        lst[i] = (lst[i] + 1) % 3 + 1
        c1 = c2 = lst[i]
        l = r = i
        b = 0
        for j in range(r, n):
            if lst[j] != c2:
                r = j - 1
                break
        else:
            r = n - 1
        for j in range(l, -1, -1):
            if lst[j] != c1:
                l = j + 1
                break
        else:
            l = 0
        if r - l - b < 3:
            val = n
        else:
            b = r - l
            while l > 0 and r < n - 1:
                c1 = lst[l - 1]
                c2 = lst[r + 1]
                if c1 != c2:
                    break
                for j in range(r + 1, n):
                    if lst[j] != c2:
                        r = j - 1
                        break
                else:
                    r = n - 1
                for j in range(l - 1, -1, -1):
                    if lst[j] != c1:
                        l = j + 1
                        break
                else:
                    l = 0
                if r - l - b < 4:
                    break
                b = r - l
            val = n - (b + 1)
        ans = min(ans, val)
        lst[i] = (lst[i] + 1) % 3 + 1
        c1 = c2 = lst[i]
        l = r = i
        b = 0
        for j in range(r, n):
            if lst[j] != c2:
                r = j - 1
                break
        else:
            r = n - 1
        for j in range(l, -1, -1):
            if lst[j] != c1:
                l = j + 1
                break
        else:
            l = 0
        if r - l - b < 3:
            val = n
        else:
            b = r - l
            while l > 0 and r < n - 1:
                c1 = lst[l - 1]
                c2 = lst[r + 1]
                if c1 != c2:
                    break
                for j in range(r + 1, n):
                    if lst[j] != c2:
                        r = j - 1
                        break
                else:
                    r = n - 1
                for j in range(l - 1, -1, -1):
                    if lst[j] != c1:
                        l = j + 1
                        break
                else:
                    l = 0
                if r - l - b < 4:
                    break
                b = r - l
            val = n - (b + 1)
        ans = min(ans, val)
        lst[i] = (lst[i] + 1) % 3 + 1
    print(ans)