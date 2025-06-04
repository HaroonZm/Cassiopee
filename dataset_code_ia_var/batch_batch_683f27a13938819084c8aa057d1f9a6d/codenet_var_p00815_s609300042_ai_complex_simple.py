from functools import reduce
from itertools import accumulate, chain, takewhile, count
N = int(input())
for _ in range(N):
    L = []
    sentinel = 0
    while True:
        numbers = list(map(int, input().split()))
        split_at_zero = lambda x: takewhile(lambda y: y != sentinel, x)
        to_extend, stop = (list(split_at_zero(numbers)), numbers[-1] == sentinel)
        L.extend(to_extend)
        if stop: break
    idxs = lambda n: list(count(n,1))
    class Stack(list):
        popz = lambda self: [self.pop() for _ in iter(lambda: self and self[-1][1]==0, False)]
    G, st, idx, S = [], Stack(), 0, idxs(0)
    for s in L:
        if s > 0:
            G.append([])
            if st:
                u, v = [idx, s-1], st[-1]
                v[1] -= 1
                G[u[0]].append(v[0])
                G[v[0]].append(u[0])
                st.append(u)
                st.popz()
            else:
                st.append([idx, s])
            idx = next(S)
        else:
            u, v = st[s-1], st[-1]
            u[1] -= 1; v[1] -= 1
            G[u[0]].append(v[0]); G[v[0]].append(u[0])
            st.popz()
    [print(i+1, *list(map(lambda x:x+1, sorted(vs)))) for i,vs in enumerate(G)]