while 1:
    n,l = map(int,raw_input().split())
    if n == 0: break
    
    tunnel = [[] for i in xrange(l-1)]
    for i in xrange(1,n+1):
        d,p = raw_input().split()
        tunnel[int(p)-1].append(i if d == "R" else -i)
    t = num = 0
    while sum(len(unit) for unit in tunnel) != 0:
        for i in xrange(l-2,-1,-1):
            for a in tunnel[i]:
                if a > 0:
                    tunnel[i].remove(a)
                    if i == l-2:
                        num = a
                    else:
                        tunnel[i+1].append(a)
        for i in xrange(l-1):
            for a in tunnel[i]:
                if a < 0:
                    tunnel[i].remove(a)
                    if i == 0:
                        num = -a
                    else:
                        tunnel[i-1].append(a)
        for i in xrange(l-1):
            if len(tunnel[i]) > 1:
                tunnel[i] = [-a for a in tunnel[i]]
        t += 1
    print t,num