while True:
    n = int(input())
    if n == 0:
        break
    v = []
    i = 0
    while i < n:
        m, a, b = map(int, input().split())
        v.append((a, m))
        v.append((b, -m))
        i += 1
    v.sort()
    s = 0
    ans = 'OK'
    j = 0
    while j < len(v):
        s += v[j][1]
        if s > 150:
            ans = 'NG'
        j += 1
    print(ans)