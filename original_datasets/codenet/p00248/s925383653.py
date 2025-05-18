while(1):
    [n,m]=map(int,raw_input().split())
    if n==0:    break
    D=[[] for i in range(n+1)]
    D[0]=range(1,n+1)
    nflg=0
    for i in range(m):
        [u,v]=map(int,raw_input().split())
        D[u].append(v)
        D[v].append(u)
        if len(D[u])>2 or len(D[v])>2:
            nflg=1
    if nflg:
        print 'no'
    else:
        bkf=0
        while (len(D[0])>0):
            st=D[0].pop()
            if len(D[st])==2:
                D[0].append(st)
            st0=st
            while len(D[st])!=0:
               nxt=D[st].pop()
               if nxt!=st0:
                   D[0].remove(nxt)
                   D[nxt].remove(st)
                   st=nxt
               else:
                   print 'no'
                   bkf=1
                   break
            if bkf:    break
        else:
            print 'yes'