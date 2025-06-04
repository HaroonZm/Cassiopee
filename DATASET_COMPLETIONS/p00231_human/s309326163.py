while True:
    n = int(input())
    if n == 0:
        break
    v = []
    for _ in range(n):
        m, a, b = map(int, input().split())
        v.append((a,m))
        v.append((b,-m))
    v.sort()
    s = 0
    ans = 'OK'
    for x in v:
        s += x[1]
        if s > 150:
            ans = 'NG'
    print(ans)