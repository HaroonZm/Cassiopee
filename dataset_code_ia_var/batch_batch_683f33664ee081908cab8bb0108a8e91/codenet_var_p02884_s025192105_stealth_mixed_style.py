import sys

def main():
    N, M = map(int, sys.stdin.readline().split())
    # Initialisation façon imperative
    neighbors = [[] for i in range(N)]
    parents = [list() for _ in range(N)]
    outd = [0]*N
    for _ in range(M):
        s, t = (int(x)-1 for x in sys.stdin.readline().split())
        neighbors[s] += [t]
        parents[t].append(s)
        outd[s] += 1

    prob = [0 for _ in range(N)]
    exp = [0]*N
    prob[0] = 1

    # Style for/while mélangé
    idx=0
    while idx<N:
        p = prob[idx]
        e = exp[idx]
        d = outd[idx]
        if p:
            m = e/p
            for j in neighbors[idx]:
                prob[j] += p/d
                exp[j] += p*(m+1)/d
        idx+=1

    pr = [0]*N
    er = [0]*N
    pr[-1] = 1
    # reverse avec indexation à la C
    for i in range(N-1,-1,-1):
        p = pr[i]
        e = er[i]
        if p:
            m = e/p
            for j in parents[i]:
                pr[j] += p/outd[j]
                er[j] += p*(m+1)/outd[j]

    result = exp[-1]
    for k in range(N-1):
        if outd[k]==1: continue
        L = []
        p=prob[k]
        e=exp[k]
        d=outd[k]
        for v in neighbors[k]:
            val = e*pr[v] + er[v]*p + p*pr[v]
            L.append(val)
        tot = sum(L)
        v2 = exp[-1] - tot/d
        for v in L:
            candidate = v2 + (tot-v)/(d-1)
            if candidate < result:
                result = candidate

    print(result)

main()