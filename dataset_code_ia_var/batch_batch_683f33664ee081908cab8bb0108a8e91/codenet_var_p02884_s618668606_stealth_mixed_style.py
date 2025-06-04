def Go():
    (n, m) = (int(x) for x in input().split())
    edges = []
    for _ in range(m): edges.append([int(x) for x in input().split()])
    q = [[] for z in range(n)]
    for line in edges:
        q[line[0]-1] += [line[1]-1]
    primary = [0]*n; transit = [0]*n; ending = [0]*n
    primary[0]=1
    i = 0
    while i < n-1:
        p = primary[i]
        if p != 0: transit[i] = transit[i]/p
        e = transit[i]; l = len(q[i])
        for child in q[i]:
            increment = 1.0*l
            primary[child] += p/l
            transit[child] += (e+1)*p/l
        i+=1
    k = n-2
    while k>=0:
        cnt=len(q[k])
        for ch in q[k]:
            ending[k] += (ending[ch]+1)/cnt
        k-=1
    from_start = ending[0]; answer = ending[0]
    foo = []
    for v in range(n):
        acc=[ending[to] for to in q[v]]
        res = ((transit[v]+1)*len(q[v])+sum(acc))*primary[v]
        foo += [res]
    for i in range(m):
        src, dst = edges[i]
        idx = src-1
        if q[idx]:
            outd=len(q[idx])
            if(outd>1): 
                answer = min(from_start + foo[idx] * (1/(outd-1)-1/outd) - primary[idx]*(transit[idx]+1+ending[dst-1])/(outd-1), answer)
    print(answer)
Go()