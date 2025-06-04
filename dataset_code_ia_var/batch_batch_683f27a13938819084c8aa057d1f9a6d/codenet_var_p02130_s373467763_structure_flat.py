N, A, B = map(int, input().split())
P = []
Q = []
ans = 0
for i in range(N):
    a, b = map(int, input().split())
    v = abs(a - b)
    if v <= A or B <= v <= 2 * A:
        ans += 1
    else:
        if a > b:
            P.append(a - b)
        else:
            Q.append(a - b)

import collections
n = 2 + len(P) + len(Q)
g = [[] for _ in range(n)]
def add_edge(fr, to, cap):
    g[fr].append([to, cap, len(g[to])])
    g[to].append([fr, 0, len(g[fr]) - 1])
for i in range(len(P)):
    add_edge(0, 2 + i, 1)
for j in range(len(Q)):
    add_edge(2 + len(P) + j, 1, 1)
for i in range(len(P)):
    for j in range(len(Q)):
        v = abs(P[i] + Q[j])
        if v <= A or B <= v <= 2 * A:
            add_edge(2 + i, 2 + len(P) + j, 1)

flow = 0
while True:
    level = [-1] * n
    deq = collections.deque()
    level[0] = 0
    deq.append(0)
    while deq:
        v = deq.popleft()
        for e in g[v]:
            if e[1] > 0 and level[e[0]] < 0:
                level[e[0]] = level[v] + 1
                deq.append(e[0])
    if level[1] < 0:
        break
    it = [0] * n
    while True:
        stack = [(0, 1 << 30)]
        route = []
        while stack:
            v, f = stack[-1]
            if v == 1:
                break
            for i in range(it[v], len(g[v])):
                e = g[v][i]
                if e[1] > 0 and level[v] < level[e[0]]:
                    it[v] = i
                    stack.append((e[0], min(f, e[1])))
                    route.append((v, i))
                    break
            else:
                it[v] = len(g[v])
                if route:
                    route.pop()
                stack.pop()
        if not stack or stack[-1][0] != 1:
            break
        d = stack[-1][1]
        for v, i in route:
            g[v][i][1] -= d
            to, _, rev = g[v][i]
            g[to][rev][1] += d
        flow += d
ans += flow
print(ans)