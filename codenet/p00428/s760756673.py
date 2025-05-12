while 1:
    n,m = map(int, raw_input().split())
    if n==m==0: break
    p = [[0,m-i] for i in xrange(1,m+1)];
    for i in xrange(n):
        mark = raw_input().split()
        for i in xrange(m): p[i][0] += int(mark[i])
    p.sort(reverse=True)
    s = [str(m-p[i][1]) for i in range(m)]
    print " ".join(s)