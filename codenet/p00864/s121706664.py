while 1:
    n,w = map(int,raw_input().split())
    if n == 0: break
    v = [0.]*11
    m = 0
    for i in range(n):
        p = int(raw_input())/w
        v[p] += 1.
        m = max(m,p)
    vm = max(v)
    ans = 0.01+sum((v[i]/vm)*(1-i*1.0/m) for i in range(m))
    print ans