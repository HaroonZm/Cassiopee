while 1:
    n,l = map(int,raw_input().split())
    if n == 0: break
    
    tube = [[] for i in xrange(l-1)]
    for i in xrange(1,n+1):
        d,p = raw_input().split()
        tube[int(p)-1].append(i if d == "R" else -i)
    t = num = 0
    while sum(len(ele) for ele in tube) != 0:
        for s in [-1,1]:
            for i in range(l-1)[::s]:
                for a in tube[i]:
                    if -s*a > 0:
                        tube[i].remove(a)
                        if i == (l-2 if s == -1 else 0):
                            num = abs(a)
                        else:
                            tube[i-s].append(a)
        for i in xrange(l-1):
            if len(tube[i]) > 1:
                tube[i] = [-a for a in tube[i]]
        t += 1
    print t,num