import sys

INF_X = float('inf')
WAYHIGH = 10**18+3

def super_merge(A1, B1, A2, B2):
    lp, rp = len(A1), len(A2)
    ret1 = [WAYHIGH]*(lp+rp)
    ret2 = [WAYHIGH]*(lp+rp)
    # style: imperative
    i = 0
    while i < lp:
        # style: classic loop
        for j in range(rp):
            # functional style min selection
            ret1[i+j] = min(ret1[i+j], A1[i]+A2[j], A1[i]+B2[j], B1[i]+A2[j])
            ret2[i+j] = min(ret2[i+j], B1[i]+B2[j])
        i += 1
    # mixed list comp and imperative
    for idx, val in enumerate(A2):
        if (val < 0) or (B2[idx] < WAYHIGH):
            for x in range(lp):
                ret1[x+idx+1] = min(ret1[x+idx+1], A1[x])
                ret2[x+idx+1] = min(ret2[x+idx+1], B1[x])
    return ret1, ret2

def parent_and_order(e, root):
    par = [None]*len(e)
    stack, ords = [root], []
    par[root] = -1
    visited = {root}
    push = stack.append
    append = ords.append
    while len(stack):
        node = stack.pop()
        append(node)
        # generator + imperative for
        for to in (x for x in e[node] if x not in visited):
            visited.add(to)
            par[to] = node
            push(to)
    return par, ords

def compute_children(par):
    r = [[] for _ in par]
    list(map(lambda v__i: r[v__i[1]].append(v__i[0]), enumerate(par[1:],1)))
    return r

read = sys.stdin.readline
n = int(read())
A = [int(i) for i in read().split()]
E = [[] for _ in range(n)]
for _ in range(n-1):
    u, v = (int(x)-1 for x in read().split())
    E[u].append(v)
    E[v].append(u)

P, O = parent_and_order(E, 0)
dpa = [[x if x<0 else WAYHIGH] for x in A]
dpb = [[x if x>0 else WAYHIGH] for x in A]
for k in O[:0:-1]:
    pk = P[k]
    dpa[pk], dpb[pk] = super_merge(dpa[pk], dpb[pk], dpa[k], dpb[k])

answ = n-1
for idd, _ in enumerate(range(n)):
    if dpa[0][idd]<0 or dpb[0][idd]<WAYHIGH:
        answ = idd
        break
print(answ)