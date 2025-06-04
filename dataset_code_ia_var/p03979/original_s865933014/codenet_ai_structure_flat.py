import sys
from collections import defaultdict

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

H, W = map(int, sys.stdin.buffer.readline().split())
S = b''.join(sys.stdin.buffer.read().split())

INF = 10 ** 12

source = -1
sink = -2
graph = defaultdict(dict)
for i in range(H * W):
    h, w = divmod(i, W)
    if S[i] == ord('.'):
        graph[i + i][i + i + 1] = 1
        graph[i + i + 1][i + i] = 0
    else:
        graph[source][i + i + 1] = INF
        graph[i + i + 1][source] = 0
    for dh, dw in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        h1 = h + dh
        w1 = w + dw
        if 0 <= h1 < H and 0 <= w1 < W:
            j = h1 * W + w1
            graph[i + i + 1][j + j] = 1
            graph[j + j][i + i + 1] = 0
        else:
            graph[i + i + 1][sink] = INF
            graph[sink][i + i + 1] = 0

V_set = set(graph)
for v in list(graph):
    for w in list(graph[v]):
        V_set.add(w)
V = list(V_set)
v_to_i = {x: i for i, x in enumerate(V)}
N = len(V)
sink_idx = v_to_i[sink]
source_idx = v_to_i[source]
g = [dict() for _ in range(N)]
for v in graph:
    vn = v_to_i[v]
    for w, c in graph[v].items():
        g[vn][v_to_i[w]] = c

level = [0] * N
from collections import deque
def bfs():
    global level
    level = [0] * N
    q = deque()
    q.append(source_idx)
    level[source_idx] = 1
    d = 1
    while q:
        if level[sink_idx]:
            break
        qq = deque()
        d += 1
        while q:
            v = q.popleft()
            for w, cap in g[v].items():
                if cap == 0:
                    continue
                if level[w]:
                    continue
                level[w] = d
                qq.append(w)
        q = qq

def dfs(v, f):
    if v == sink_idx:
        return f
    for _ in range(len(itr[v])):
        try:
            w, cap = next(itr[v])
        except StopIteration:
            continue
        if cap == 0 or level[w] != level[v] + 1:
            continue
        d = dfs(w, min(f, cap))
        if d:
            g[v][w] -= d
            g[w][v] += d
            return d
    return 0

INF_FLOW = 10 ** 18
flow = 0
while True:
    bfs()
    if level[sink_idx] == 0:
        break
    itr = [iter(e.items()) for e in g]
    while True:
        f = dfs(source_idx, INF_FLOW)
        if f == 0:
            break
        flow += f
answer = flow if flow < INF else -1
print(answer)