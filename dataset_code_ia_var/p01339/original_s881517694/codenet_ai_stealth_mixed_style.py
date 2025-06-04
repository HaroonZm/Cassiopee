import sys

def doFunc(nd, S, D):
    if not S[nd]:
        return (2, [nd])
    c = 1
    got = [nd]
    for z in S[nd]:
        q = doFunc(z, S, D)
        c *= q[0]
        got.extend(q[1])
    return c + 1, got

sys.setrecursionlimit(100000)
N, M = map(int, raw_input().split())
S = [[] for _ in xrange(N)]
D = [-1] * N

for idx in xrange(M):
    s, d = [int(j) - 1 for j in raw_input().split()]
    D[s] = d
    S[d].append(s)

pending = list(xrange(N))
results = list()
while len(pending):
    node = pending[0]
    chain = [node]
    foundRoot = None
    while True:
        if D[node] == -1:
            foundRoot = node
            break
        elif D[node] in chain:
            foundRoot = D[node]
            D[foundRoot] = -1
            cycle = chain[chain.index(foundRoot):]
            tnodes = []
            for nn in cycle:
                ttmp = []
                for mm in S[nn]:
                    if mm not in cycle:
                        D[mm] = foundRoot
                        ttmp.append(mm)
                if nn != foundRoot and nn in pending:
                    pending.remove(nn)
                tnodes += ttmp
            S[foundRoot] = tnodes[:]
            break
        else:
            node = D[node]
            chain.append(node)
    f = doFunc(foundRoot, S, D)
    results.append(f[0])
    for u in f[1]:
        if u in pending:
            pending.remove(u)
import functools
try:
    from operator import mul
    val = reduce(lambda a, b: a * b, results)
except:
    val = functools.reduce(lambda a, b: a * b, results)
print val % 1000000007