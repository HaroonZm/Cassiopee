n, k = map(int, input().split())
s = input()
m = min(s)
for p in range(k):
    u = s + s[::-1]
    l = []
    cnt = 0
    idx = 0
    for i in range(n * 2):
        if u[i] == m:
            if cnt == 0:
                idx = i
            cnt += 1
        else:
            if cnt > 0:
                l.append((cnt, idx))
                cnt = 0
    if cnt > 0:
        l.append((cnt, idx))
    a, j = max(l)
    if a >= n:
        print(m * n)
        exit(0)
    for c, i in l:
        if i <= n and c == a:
            s = min(s, u[i:i + n])
    s = s[::-1]
print(s[::-1])