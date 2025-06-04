import sys
import heapq

INF = 10**18

readline = sys.stdin.readline
write = sys.stdout.write

N = int(readline())
W = [list(map(int, readline().split())) for _ in range(N)]
E = [list(map(int, readline().split())) for _ in range(N)]
F = [readline() for _ in range(N)]

node_count = 2*N+2
G = [[] for _ in range(node_count)]

for i in range(N):
    Wi = W[i]
    Ei = E[i]
    Fi = F[i]
    s0 = sum(Ei[j] for j in range(N) if Fi[j] == "o")
    for j in range(N):
        if Fi[j] == "o":
            s = s0 - Ei[j]
        else:
            s = s0 + Wi[j]
        # add_edge(i, N+j, 1, s)
        G[i].append([N+j, 1, s, len(G[N+j])])
        G[N+j].append([i, 0, -s, len(G[i])-1])
    # add_edge(2*N, i, 1, 0)
    G[2*N].append([i, 1, 0, len(G[i])])
    G[i].append([2*N, 0, 0, len(G[2*N])-1])
    # add_edge(N+i, 2*N+1, 1, 0)
    G[N+i].append([2*N+1, 1, 0, len(G[2*N+1])])
    G[2*N+1].append([N+i, 0, 0, len(G[N+i])-1])

s = 2*N
t = 2*N+1
f = N

res = 0
H = [0]*node_count
prv_v = [0]*node_count
prv_e = [0]*node_count

while f:
    dist = [INF]*node_count
    dist[s] = 0
    que = [(0, s)]
    while que:
        c, v = heapq.heappop(que)
        if dist[v] < c:
            continue
        for i, (w, cap, cost, _) in enumerate(G[v]):
            if cap > 0 and dist[w] > dist[v] + cost + H[v] - H[w]:
                new_dist = dist[v] + cost + H[v] - H[w]
                dist[w] = new_dist
                prv_v[w] = v
                prv_e[w] = i
                heapq.heappush(que, (new_dist, w))
    if dist[t] == INF:
        res = -1
        break
    for i in range(node_count):
        H[i] += dist[i]
    d = f
    v = t
    while v != s:
        pv = prv_v[v]
        pe = prv_e[v]
        d = min(d, G[pv][pe][1])
        v = pv
    f -= d
    res += d * H[t]
    v = t
    while v != s:
        pv = prv_v[v]
        pe = prv_e[v]
        e = G[pv][pe]
        e[1] -= d
        rev_idx = e[3]
        G[v][rev_idx][1] += d
        v = pv

write("%d\n" % res)
ans = []
for i in range(N):
    Gi = G[i]
    Wi = W[i]
    Ei = E[i]
    Fi = F[i]
    for j in range(N):
        if Gi[j][1] == 0:
            for k in range(N):
                if j == k or Fi[k] == ".":
                    continue
                ans.append("%d %d erase" % (i+1, k+1))
            if Fi[j] == ".":
                ans.append("%d %d write" % (i+1, j+1))
            break
write("%d\n" % len(ans))
if ans:
    write("\n".join(ans))
    write("\n")