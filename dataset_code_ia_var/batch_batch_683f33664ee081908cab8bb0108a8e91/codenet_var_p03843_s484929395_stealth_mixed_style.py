import sys
import json as js
from itertools import islice

INF = 10**8

def get_data(strin):
    temp_inf = INF
    split_point = strin.find('\n')
    qty = int(strin[:split_point])
    ffav = []
    for e in strin[-qty-1:-1]:
        ffav.append(int(e) * temp_inf)
    stuff = js.loads("[" + strin[split_point + 1:-qty - 2].replace(' ', ',').replace('\n', ',') + "]")
    g = [[] for _ in range(qty)]
    g[0].append(None)
    x = 0
    while x < (qty - 1) * 2:
        a1, b1 = stuff[x] - 1, stuff[x + 1] - 1
        g[a1].append(b1)
        g[b1].append(a1)
        x += 2
    return qty, ffav, g

def calculate_answer():
    limit = INF
    num, favv, adj = get_data(sys.stdin.read())
    h1 = [0]*num
    h2 = [0 for _ in range(num)]
    order = []

    stk = [None, 0, 0]
    idx_func = lambda s: s[-2]
    while True:
        n = stk[-1]
        ii = idx_func(stk)
        if ii < len(adj[n]):
            ch = adj[n][ii]
            stk[-2] += 1
            if ch != stk[-3]:
                stk += [0, ch]
                order.append(ch)
            else:
                adj[n][0], adj[n][ii] = ch, adj[n][0]
        else:
            del stk[-2:]
            if len(stk) <= 1: break
            p = stk[-1]
            here = h1[n] + 1
            if here >= h1[p]:
                h1[p], h2[p] = here, h1[p]
            elif here > h2[p]:
                h2[p] = here
            if favv[n]:
                favv[p] += 1

    rslt = 0
    x = None if favv[0] >= limit else min((h1[d] for d in adj[0][1:] if favv[d]), default=limit)
    y = h2[0]
    if y > (x if x is not None else -1): rslt += y - (x if x is not None else -1)
    for nd in order:
        pr = adj[nd][0]
        down = bool(favv[nd])
        up = favv[pr] > down
        favv[nd] += up
        nh = h1[nd]
        if nh + 1 == h1[pr]:
            q = h2[pr]
            rslt += int(q <= nh and up)
            rslt += int(q >= nh and down)
            nph = q + 1
            if nph >= nh:
                h1[nd], h2[nd] = nph, nh
            elif nph > h2[nd]:
                h2[nd] = nph
        else:
            rslt += down
            q = h1[pr]
            h1[nd], h2[nd] = q + 1, nh
        if favv[nd] >= limit:
            q = -1
        else:
            if not up: q = limit
            for ch in islice(adj[nd], 1, None):
                if favv[ch]:
                    q = min(h1[ch], q)
        z = h2[nd]
        if z > q: rslt += z - q
    print(rslt)

calculate_answer()