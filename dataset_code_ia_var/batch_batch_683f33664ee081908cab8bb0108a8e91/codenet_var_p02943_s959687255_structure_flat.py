n, k = map(int, input().split())
s = input()
m = min(s)
p = 0
while p < k:
    u = s + s[::-1]
    l = []
    cnt = 0
    idx = 0
    i = 0
    while i < n * 2:
        if u[i] == m:
            if cnt == 0:
                idx = i
            cnt += 1
        else:
            if cnt > 0:
                l.append((cnt, idx))
                cnt = 0
        i += 1
    if cnt > 0:
        l.append((cnt, idx))
    a, j = 0, 0
    for x, y in l:
        if x > a:
            a, j = x, y
    if a >= n:
        print(m * n)
        exit(0)
    t = s
    for c, i in l:
        if i <= n and c == a:
            if u[i:i + n] < t:
                t = u[i:i + n]
    s = t[::-1]
    p += 1
print(s[::-1])