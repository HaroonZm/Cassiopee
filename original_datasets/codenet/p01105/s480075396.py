a=65280; b=61680; c=52428; d=43690; e=65535
from heapq import heappush, heappop
Q = [(1, a), (1, b), (1, c), (1, d)]
L = {a: 1, b: 1, c: 1, d: 1, e: 1, e: 1, 0: 1}
H = []
get = L.get
push = H.append
while Q:
    l, p = heappop(Q)
    if L[p] < l: continue
    if l+1 < get(p ^ e, 17):
        L[p ^ e] = l+1
        l < 15 and heappush(Q, (l+1, p ^ e))
    if l < 13:
        li = 13-l; l3 = 3+l
        for q, r in H:
            if r <= li:
                k = p & q
                if r < get(k, 17)-l3:
                    L[k] = l3+r
                    r < li and heappush(Q, (l3+r, k))
                k = p ^ q
                if r < get(k, 17)-l3:
                    L[k] = l3+r
                    r < li and heappush(Q, (l3+r, k))
            else: break
    if l < 7: push((p, l))
print(*map(L.__getitem__, eval("e&"+",e&".join(open(0).read().replace(*"-~").replace(*"*&").replace(*"1e").split()[:-1]))),sep='\n')