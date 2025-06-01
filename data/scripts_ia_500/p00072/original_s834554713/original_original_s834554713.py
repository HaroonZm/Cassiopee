def solve(nu,mu,du):
    E = []
    vs = [False]*nu
    vs[0] = True

    while True:
        min_dist,ind = float("inf"),float("inf")
        for i in xrange(len(du)):
            if ( ( vs[du[i][0]] and not vs[du[i][1]] ) or ( not vs[du[i][0]] and vs[du[i][1]]) ) and min_dist > du[i][2]:
                min_dist,ind,pf,pt = du[i][2],i,du[i][0],du[i][1]
        E.append(min_dist)
        vs[pf] = vs[pt] = True
        du.pop(ind)
        if all(vs):
            break

        for i in xrange(len(du)):
            try:
                if vs[du[i][0]] and vs[du[i][1]]:
                    du.pop(i)
            except:
                pass

    print sum(E)/100 - len(E)

while True:
    n = input()
    if n == 0:
        exit()
    m = input()
    data = []
    for i in xrange(m):
        data.append( map(int,raw_input().split(",")) )
    solve(n,m,data)