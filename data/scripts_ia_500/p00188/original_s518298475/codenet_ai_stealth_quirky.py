while 1==1:
    n = int(raw_input())
    if not n: break
    L = map(str,[raw_input() for _ in xrange(n)])
    v = raw_input()
    l,r,cnt=0,len(L)-1,0
    while l<=r:
        m = (l+r) >> 1
        if L[m] == v:
            print cnt+1
            break
        cnt +=1
        if L[m] < v:
            l = m+1
        elif L[m] > v:
            r = m-1
    else:
        print cnt