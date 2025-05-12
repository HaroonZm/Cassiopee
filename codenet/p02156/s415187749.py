from collections import deque

N,M = map(int,input().split())
U = input()
A = list(map(int,input().split()))
src = [tuple(map(int,input().split())) for i in range(M)]

edges = {}
for s,t,b in src:
    s,t = s-1,t-1
    if s>t: s,t = t,s
    if (s,t) in edges:
        edges[(s,t)] += b
    else:
        edges[(s,t)] = b

P = N+2
es = [[] for i in range(P)] # [[to1,cap1,rev1], ...]

def add_edge(fr,to,cap):
    es[fr].append([to,cap,len(es[to])])
    es[to].append([fr,0,len(es[fr])-1])

for i,(u,a) in enumerate(zip(U,A)):
    if u == 'L':
        add_edge(0,i+2,a)
        add_edge(i+2,1,0)
    else:
        add_edge(0,i+2,0)
        add_edge(i+2,1,a)
for (s,t),b in edges.items():
    add_edge(t+2,s+2,b)

INF = float('inf')
level = [0] * P
iters = [0] * P

def dinic_max_flow(s,t):
    global iters

    def _bfs(s):
        global level
        level = [-1] * P
        level[s] = 0
        q = deque([s])
        while q:
            v = q.popleft()
            for to,cap,rev in es[v]:
                if cap > 0 and level[to] < 0:
                    level[to] = level[v] + 1
                    q.append(to)

    def _dfs(v,t,f):
        if v == t: return f
        for i in range(iters[v],len(es[v])):
            iters[v] += 1
            to,cap,rev = es[v][i]
            if es[v][i][1] > 0 and level[v] < level[to]:
                d = _dfs(to,t,min(f,es[v][i][1]))
                if d > 0:
                    es[v][i][1] -= d #cap
                    es[to][rev][1] += d
                    return d
        return 0

    flow = 0
    while True:
        _bfs(s)
        if level[t] < 0: return flow
        iters = [0] * P
        f = 0
        while True:
            f = _dfs(s,t,INF)
            if f <= 0: break
            flow += f

print(dinic_max_flow(0,1))