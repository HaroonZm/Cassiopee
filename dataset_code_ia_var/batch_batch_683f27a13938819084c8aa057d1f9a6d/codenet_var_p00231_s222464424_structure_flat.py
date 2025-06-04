while 1:
    n = input()
    if n == 0:
        break
    d = []
    for i in range(n):
        d.append(list(map(int, raw_input().split())))
    w = 0
    for d1 in d:
        s = 0
        for d2 in d:
            if d2[1] <= d1[1] < d2[2]:
                s += d2[0]
        if s > w:
            w = s
    if w < 151:
        print "OK"
    else:
        print "NG"