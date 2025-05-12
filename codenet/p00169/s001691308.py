while True:
    h = map(int, raw_input().split())
    if h[0] == 0:
        break
    t = 0
    a = 0
    for c in sorted(h, reverse=True):
        if 2 <= c <= 9:
            t += c
        elif 10 <= c:
            t += 10
        elif c == 1:
            a += 1
            
    t += a
    if 21 < t:
        print 0
    else:
        for i in range(a):
            if 21 < t + 10:
                print t
                break
            else:
                t += 10
        else:
            print t