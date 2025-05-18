ref = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
while 1:
    N,M,Q = map(int,raw_input().split())
    if N == 0: break
    sn = set(range(N))
    corr = [set(range(N)) for _ in range(M)]
    s = [0]*N
    for loop in xrange(Q):
        S,B = raw_input().split()
        s = [1-s[i] if S[i] == "1" else s[i] for i in range(N)]
        on  = set([i for i in range(N) if s[i]])
        off = sn-on
        for i in range(M):
            corr[i] &= on if B[i] == "1" else off
    ans = [ref[list(i)[0]] if len(i) == 1 else "?" for i in corr]
    print "".join(ans)