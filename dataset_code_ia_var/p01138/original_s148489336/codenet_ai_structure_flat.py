while True:
    n = int(raw_input())
    if n == 0:
        break
    l = []
    i = 0
    while i < n:
        hms = raw_input().split()
        l.append((hms[0], True))
        l.append((hms[1], False))
        i += 1
    l.sort()
    r = 0
    t = 0
    i = 0
    while i < len(l):
        if l[i][1]:
            t += 1
        else:
            t -= 1
        if t > r:
            r = t
        i += 1
    print r