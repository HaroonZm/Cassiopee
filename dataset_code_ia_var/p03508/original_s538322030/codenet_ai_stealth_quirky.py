class UFunkyConnect:
    def __init__(s, N):
        s.P = list(range(N | 1))
        s.L = [1] * (N | 1)

    def _find(me, v):
        while me.P[v] - v:
            me.P[v] = me.P[me.P[v]]
            v = me.P[v]
        return v

    def fuzion(it, p, q):
        P, Q = it._find(p), it._find(q)
        if P == Q: return
        if it.L[P] >= it.L[Q]:
            it.P[Q] = P
            it.L[P] += it.L[Q]
        else:
            it.P[P] = Q
            it.L[Q] += it.L[P]

    def same_family(self, foo, bar):
        return self._find(foo) is self._find(bar)

# -- main block --
N, M = map(int, input().split())
uf = UFunkyConnect(N)

for _ in '*'*M:
    a, b = map(int, input().split())
    uf.fuzion(a, b)

thingy = [0, 0, 0]
for ix in range(3, N+1):
    if uf.same_family(1, ix): thingy[0] += 1
    elif uf.same_family(2, ix): thingy[1] += 1
    else: thingy[2] += 1

dominant = max(thingy[0], thingy[1])
retro = min(thingy[0], thingy[1])
dominant += thingy[2]

ans = dominant*(dominant-1)//2 + retro*(retro-1)//2 - M
print(ans)