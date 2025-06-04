s = [0] * 30001
while True:
    n_m = input().split()
    n = int(n_m[0])
    m = int(n_m[1])
    if n == 0:
        break

    f = [-1] * m
    sum_a = 0
    nmax = 0
    ans = 0
    a = list(map(int, input().split()))
    for i in range(n):
        sum_a += a[i]
        a[i] = a[i] % m
        if a[i] > nmax:
            nmax = a[i]
        if a[i] == m - 1:
            ans = a[i]
        s[i + 1] = s[i] + a[i]
        if s[i + 1] >= m:
            s[i + 1] -= m
        f[s[i + 1]] = i + 1

    if ans == 0:
        if nmax == 0:
            ans = 0
        elif sum_a < m:
            ans = sum_a
        else:
            found = False
            ans_val = 0
            for val in range(m - 1, nmax - 1, -1):
                for i in range(n + 1):
                    x = s[i] + val
                    if x >= m:
                        x -= m
                    if f[x] >= i:
                        found = True
                        ans_val = val
                        break
                if found:
                    ans = ans_val
                    break
    print(ans)