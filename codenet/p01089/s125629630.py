while 1:
    n = input()
    if n == 0:
        break
    s = raw_input()
    Q = set()
    lock = 0
    P = []
    for c in s:
        if c is 'u':
            lock = 0
        else:
            v = (lock, 1 << int(c))
            if v not in Q:
                P.append(v)
                Q.add(v)
            lock |= 1 << int(c)
    i = 0; ok = 1
    while i < len(P) and ok:
        lock1, t1 = P[i]
        if lock1 & t1 == t1:
            ok = 0
        for j in xrange(i):
            lock2, t2 = P[j]
            if lock1 & lock2 == 0 and t1 & lock2 == t1:
                if t2 & lock1 == t2:
                    ok = 0
                v = (lock1 | lock2, t2)
                if v not in Q:
                    P.append(v)
                    Q.add(v)
        i += 1
    print "SAFE"*ok or "UNSAFE"