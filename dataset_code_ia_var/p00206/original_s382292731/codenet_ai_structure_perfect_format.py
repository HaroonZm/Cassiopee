while True:
    L = input()
    if L < 1:
        break
    a, t = 0, 0
    for i in range(12):
        k = map(int, raw_input().split())
        t += k[0] - k[1]
        if L <= t:
            a += 1
    if a:
        print 12 - a + 1
    else:
        print "NA"