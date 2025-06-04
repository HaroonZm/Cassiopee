while True:
    n, m = map(int, raw_input().split())
    if n == 0 and m == 0:
        break
    p = []
    for i in range(m):
        p.append([0, m - (i + 1)])
    for i in range(n):
        mark = raw_input().split()
        for j in range(m):
            p[j][0] += int(mark[j])
    p.sort(reverse=True)
    s = []
    for i in range(m):
        s.append(str(m - p[i][1]))
    print " ".join(s)