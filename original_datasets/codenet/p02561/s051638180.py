import os
import sys

import numpy as np

def solve(n, m, sss):
    BIT_SHIFT = 9
    BIT_MASK = (1 << BIT_SHIFT) - 1

    def combine_rc(r, c):
        return (r << BIT_SHIFT) | c

    def separate_rc(rc):
        return rc >> BIT_SHIFT, rc & BIT_MASK

    DINIC_LINKS = []

    def dinic_init(n):
        lst = [[0, 0, 0]]
        lst.clear()
        DINIC_LINKS.append([lst.copy() for _ in range(n)])
        return len(DINIC_LINKS) - 1

    def dinic_add_link(ins, frm, to, cap):
        links = DINIC_LINKS[ins]
        links[frm].append([to, cap, len(links[to])])
        links[to].append([frm, 0, len(links[frm]) - 1])

    def dinic_bfs(ins, n, s):
        links = DINIC_LINKS[ins]
        depth = np.full(n, -1, dtype=np.int64)
        depth[s] = 0
        deq = np.zeros(n + 5, dtype=np.int64)
        dl, dr = 0, 1
        deq[0] = s
        while dl < dr:
            v = deq[dl]
            dl += 1
            for link in links[v]:
                if link[1] > 0 and depth[link[0]] == -1:
                    depth[link[0]] = depth[v] + 1
                    deq[dr] = link[0]
                    dr += 1
        return depth

    def dinic_dfs(ins, depth, progress, s, t):
        links = DINIC_LINKS[ins]
        stack = [(s, 10 ** 18)]
        flow = 0
        while stack:
            v, f = stack.pop()
            if v == t:
                flow = f
                continue
            if flow == 0:
                i = progress[v]
                if i == len(links[v]):
                    continue
                progress[v] += 1
                stack.append((v, f))
                to, cap, rev = links[v][i]
                if cap == 0 or depth[v] >= depth[to]:
                    continue
                stack.append((to, min(f, cap)))
            else:
                i = progress[v] - 1
                link = links[v][i]
                link[1] -= flow
                links[link[0]][link[2]][1] += flow
        return flow

    def dinic_maximum_flow(ins, n, s, t):
        flow = 0
        while True:
            depth = dinic_bfs(ins, n, s)
            if depth[t] == -1:
                return flow
            progress = np.zeros(n, dtype=np.int64)
            path_flow = dinic_dfs(ins, depth, progress, s, t)
            while path_flow != 0:
                flow += path_flow
                path_flow = dinic_dfs(ins, depth, progress, s, t)

    lefts = []
    rights = []
    rights_rev = {}

    for r in range(1, n + 1):
        for c in range(1, m + 1):
            if sss[r, c]:
                continue
            rc = combine_rc(r, c)
            if (r ^ c) & 1:
                lefts.append(rc)
            else:
                rights_rev[rc] = len(rights)
                rights.append(rc)
    l_size = len(lefts)
    r_size = len(rights)
    s = l_size + r_size
    t = s + 1
    total_size = t + 1

    ins = dinic_init(total_size)

    MOVE = (-(1 << BIT_SHIFT), -1, 1, 1 << BIT_SHIFT)

    for i in range(l_size):
        rc = lefts[i]
        for drc in MOVE:
            nrc = rc + drc
            if nrc in rights_rev:
                dinic_add_link(ins, i, rights_rev[nrc] + l_size, 1)
        dinic_add_link(ins, s, i, 1)
    for j in range(r_size):
        dinic_add_link(ins, j + l_size, t, 1)

    flow = dinic_maximum_flow(ins, total_size, s, t)
    links = DINIC_LINKS[ins]

    for i in range(l_size):
        for link in links[i]:
            if link[0] == s or link[1] == 1:
                continue
            j = link[0] - l_size
            ir, ic = separate_rc(lefts[i])
            jr, jc = separate_rc(rights[j])
            if ir == jr:
                if ic > jc:
                    ic, jc = jc, ic
                sss[ir, ic] = 4
                sss[jr, jc] = 5
            else:
                if ir > jr:
                    ir, jr = jr, ir
                sss[ir, ic] = 2
                sss[jr, jc] = 3
            break

    return flow

SIGNATURE = '(i8,i8,i1[:,:],)'
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

n, m = map(int, input().split())
sss = np.ones((n + 2, m + 2), dtype=np.int8)
for i in range(n):
    sss[i + 1, 1:m + 1] = list(map('.#'.index, input()))

ans = solve(n, m, sss)
print(ans)
CHARS = '.#v^><'.__getitem__
for i in range(1, n + 1):
    print(''.join(map(CHARS, sss[i, 1:m + 1])))