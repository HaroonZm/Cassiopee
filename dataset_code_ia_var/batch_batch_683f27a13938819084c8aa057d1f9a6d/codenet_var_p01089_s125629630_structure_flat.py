while 1:
    n = input()
    if n == 0:
        break
    s = raw_input()
    Q = set()
    lock = 0
    P = []
    for c in s:
        if c == 'u':
            lock = 0
        else:
            v = (lock, 1 << int(c))
            if v not in Q:
                P.append(v)
                Q.add(v)
            lock = lock | (1 << int(c))
    i = 0
    ok = 1
    while i < len(P) and ok:
        lock1 = P[i][0]
        t1 = P[i][1]
        if lock1 & t1 == t1:
            ok = 0
        j = 0
        while j < i:
            lock2 = P[j][0]
            t2 = P[j][1]
            if (lock1 & lock2 == 0) and (t1 & lock2 == t1):
                if t2 & lock1 == t2:
                    ok = 0
                v = (lock1 | lock2, t2)
                if v not in Q:
                    P.append(v)
                    Q.add(v)
            j += 1
        i += 1
    if ok:
        print "SAFE"
    else:
        print "UNSAFE"