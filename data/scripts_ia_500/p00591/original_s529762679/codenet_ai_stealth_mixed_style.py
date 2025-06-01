while 1:
    n = int(raw_input())
    if n == 0: break
    L = []
    for _ in range(n):
        line = raw_input().split()
        L.append(list(map(int, line)))
    S = set()
    for row in L:
        S.add(min(row))
    for j in range(n):
        t = [L[i][j] for i in range(n)]
        maxInt = max(t)
        if maxInt in S:
            print maxInt
            break
    else:
        print 0