import sys
from heapq import heappush, heappop

V, E, r = list(map(int, input().split()))
Edge = [list(map(int, input().split())) for _ in range(E)]

stack = []
params = []
result = None
stack.append((V, Edge, r))

while stack:
    V, Edge, r = stack.pop()
    if V <= 1:
        result = 0
        continue
    q = [[] for _ in range(V)]
    for s, t, w in Edge:
        heappush(q[t], (w, s))
    M = [(0, -1) for _ in range(V)]
    for t in range(V):
        if t != r and len(q[t]) > 0:
            w, s = heappop(q[t])
            M[t] = (w, s)
    used = [False for _ in range(V)]
    hist = []
    cycle = []
    for t in range(V):
        w, s = M[t]
        if s == -1 or used[t]:
            continue
        if not used[t]:
            used[t] = True
            hist = [t]
            tt = s
            while not used[tt]:
                used[tt] = True
                hist.append(tt)
                w2, s2 = M[tt]
                if s2 == -1:
                    hist = []
                    break
                tt = s2
            if tt in hist and len(hist) > 0 and s2 != -1:
                try:
                    k = hist.index(tt)
                    cycle = hist[k:]
                except Exception:
                    continue
                break
    if len(cycle) == 0:
        print(sum(m[0] for m in M))
        sys.exit()
    parent = min(cycle)
    rn = [0] * V
    k = 0
    for t in range(V):
        if k == parent:
            k += 1
        if t in cycle:
            rn[t] = parent
        else:
            rn[t] = k
            k += 1
    Vp = V - len(cycle) + 1
    Ep = []
    for s, t, w in Edge:
        if s in cycle:
            if t in cycle:
                continue
            else:
                Ep.append([parent, rn[t], w])
        else:
            if t in cycle:
                Ep.append([rn[s], parent, w - M[t][0]])
            else:
                Ep.append([rn[s], rn[t], w])
    r2 = rn[r]
    stack.append((Vp, Ep, r2))
    cycle_sum = sum(M[t][0] for t in cycle)
    params.append(cycle_sum)

if result is not None:
    print(result + sum(params))