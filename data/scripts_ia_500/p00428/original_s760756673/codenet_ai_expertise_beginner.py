while True:
    line = raw_input()
    n, m = line.split()
    n = int(n)
    m = int(m)
    if n == 0 and m == 0:
        break
    p = []
    for i in range(1, m+1):
        p.append([0, m - i])
    for _ in range(n):
        marks = raw_input().split()
        for i in range(m):
            p[i][0] = p[i][0] + int(marks[i])
    p.sort(reverse=True)
    s = []
    for i in range(m):
        s.append(str(m - p[i][1]))
    print " ".join(s)