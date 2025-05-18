import os
import sys
from heapq import heappop, heappush

import numpy as np

def solve(n, m, field):
    MINCOSTFLOW_LINKS = []
    INF = 10 ** 10

    def mincostflow_init(n):
        """ n: 頂点数 """
        lst = [[0]]
        lst.clear()
        MINCOSTFLOW_LINKS.append([lst.copy() for _ in range(n)])
        return len(MINCOSTFLOW_LINKS) - 1

    def mincostflow_add_link(ins, frm, to, capacity, cost):
        """ インスタンスID, 辺始点頂点番号, 辺終点頂点番号, 容量, コスト """
        links = MINCOSTFLOW_LINKS[ins]
        links[frm].append([to, capacity, cost, len(links[to])])
        links[to].append([frm, 0, -cost, len(links[frm]) - 1])

    def mincostflow_flow(ins, s, t, quantity):
        """ インスタンスID, フロー始点頂点番号, フロー終点頂点番号, 要求流量 """
        links = MINCOSTFLOW_LINKS[ins]
        n = len(links)
        res = 0
        potentials = np.zeros(n, dtype=np.int64)
        dist = np.full(n, INF, dtype=np.int64)
        prev_v = np.full(n, -1, dtype=np.int64)
        prev_e = np.full(n, -1, dtype=np.int64)

        while quantity:
            dist.fill(INF)
            dist[s] = 0
            que = [(0, s)]

            while que:
                total_cost, v = heappop(que)
                if dist[v] < total_cost:
                    continue
                for i, (u, cap, cost, _) in enumerate(links[v]):
                    new_cost = dist[v] + potentials[v] - potentials[u] + cost
                    if cap > 0 and new_cost < dist[u]:
                        dist[u] = new_cost
                        prev_v[u] = v
                        prev_e[u] = i
                        heappush(que, (new_cost, u))

            # Cannot flow quantity
            if dist[t] == INF:
                return -1

            potentials += dist

            cur_flow = quantity
            v = t
            while v != s:
                cur_flow = min(cur_flow, links[prev_v[v]][prev_e[v]][1])
                v = prev_v[v]
            quantity -= cur_flow
            res += cur_flow * potentials[t]

            v = t
            while v != s:
                link = links[prev_v[v]][prev_e[v]]
                link[1] -= cur_flow
                links[v][link[3]][1] += cur_flow
                v = prev_v[v]

        return res

    nm = (n + 2) * (m + 2)
    m2 = m + 2

    starts = np.where(field == 1)[0]
    s_size = starts.size

    ins = mincostflow_init(nm + s_size + 2)
    s = nm + s_size
    t = s + 1

    stack = np.zeros(10 ** 7, np.int64)
    SENTINEL = INF - 1

    for i in range(s_size):
        mincostflow_add_link(ins, s, nm + i, 1, 0)

        stack[0] = starts[i]
        stack[1] = 0
        sl = 0
        sr = 2
        stacked = np.zeros(nm, np.int8)
        stacked[starts[i]] = 1
        while sl < sr:
            v = stack[sl]
            c = stack[sl + 1]
            sl += 2

            mincostflow_add_link(ins, nm + i, v, 1, SENTINEL - c)

            if stacked[v + 1] == 0 and field[v + 1] != 2:
                stack[sr] = v + 1
                stack[sr + 1] = c + 1
                stacked[v + 1] = 1
                sr += 2
            if stacked[v + m2] == 0 and field[v + m2] != 2:
                stack[sr] = v + m2
                stack[sr + 1] = c + 1
                stacked[v + m2] = 1
                sr += 2

    for i in range(nm):
        if field[i] != 2:
            mincostflow_add_link(ins, i, t, 1, 0)

    f = mincostflow_flow(ins, s, t, s_size)

    ans = SENTINEL * s_size - f
    return ans

SIGNATURE = '(i8,i8,i1[:],)'
if sys.argv[-1] == 'ONLINE_JUDGE':
    from numba.pycc import CC

    cc = CC('my_module')
    cc.export('solve', SIGNATURE)(solve)
    cc.compile()
    exit()

if os.name == 'posix':
    # noinspection PyUnresolvedReferences
    from my_module import solve
else:
    from numba import njit

    solve = njit(SIGNATURE, cache=True)(solve)
    print('compiled', file=sys.stderr)

n, m = map(int, sys.stdin.readline().split())
field = '#' * (m + 3) + '##'.join(sys.stdin.read().split()) + '#' * (m + 3)
field = np.fromiter(map('.o#'.index, field), np.int8)
ans = solve(n, m, field)
print(ans)