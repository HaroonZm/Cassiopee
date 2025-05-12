while 1:
    n,l = map(int,raw_input().split())
    if n == 0: break
    R = [0]*(l-1)
    L = [0]*(l-1)
    for i in xrange(1,n+1):
        d,p = raw_input().split()
        p = int(p)-1
        if d == "R": R[p] = i
        else: L[p] = i
    t = num = 0
    while sum(R)+sum(L) != 0:
        if R[-1] > 0: num = R[-1]
        R = [0]+R[:-1]
        if L[0]  > 0: num = L[0]
        L = L[1:]+[0]
        for i in xrange(l-1):
            if min(L[i],R[i]) > 0: R[i],L[i] = L[i],R[i]
        t += 1
    print t,num