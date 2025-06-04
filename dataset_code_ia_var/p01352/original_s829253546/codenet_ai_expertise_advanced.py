import sys
import array
from collections import defaultdict, deque

readline = sys.stdin.readline
write = sys.stdout.write

def solve():
    N, K = map(int, readline().split())
    ES = [tuple(map(int, readline().split())) for _ in range(K)]
    emp = defaultdict(int)
    BLOCK = int(K**0.5) + 1

    # Faster union-find with path compression & union by rank
    par = array.array('i', range(N))
    rank = array.array('B', (0,)*N)

    def root(x):
        px = par[x]
        if px != x:
            par[x] = root(px)
        return par[x]

    def unite(x, y):
        rx, ry = root(x), root(y)
        if rx == ry: return
        if rank[rx] < rank[ry]:
            par[rx] = ry
        else:
            par[ry] = rx
            if rank[rx] == rank[ry]:
                rank[rx] += 1

    used = array.array('I', (0,)*N)
    lb = 0

    for block in range(0, K, BLOCK):
        par[:] = range(N)
        rank[:] = (0,)*N

        active = set()
        for j in range(block, min(block+BLOCK, K)):
            t, a, b = ES[j]
            if t == 3: continue
            e = (a, b)
            if emp[e]:
                active.add(e)
            emp[e] = 0

        for (v, w), d in emp.items():
            if d:
                unite(v, w)

        G = [[] for _ in range(N)]
        edge_cnt = {}

        for a, b in active:
            ra, rb = root(a), root(b)
            if ra == rb: continue
            e = tuple(sorted((ra, rb)))
            if e not in edge_cnt:
                edge_cnt[e] = [ [rb, 1], [ra, 1] ]
                G[ra].append(edge_cnt[e][0])
                G[rb].append(edge_cnt[e][1])
            else:
                edge_cnt[e][0][1] = edge_cnt[e][1][1] = edge_cnt[e][0][1] + 1

        for j in range(block, min(block+BLOCK, K)):
            t, a, b = ES[j]
            ra, rb = root(a), root(b)
            e = tuple(sorted((ra, rb)))
            if t == 1:
                emp[(a, b)] = 1
                if ra == rb:
                    continue
                if e not in edge_cnt:
                    edge_cnt[e] = [ [rb, 1], [ra, 1] ]
                    G[ra].append(edge_cnt[e][0])
                    G[rb].append(edge_cnt[e][1])
                else:
                    edge_cnt[e][0][1] = edge_cnt[e][1][1] = edge_cnt[e][0][1] + 1
            elif t == 2:
                emp[(a, b)] = 0
                if ra == rb: continue
                e1, e2 = edge_cnt[e]
                e1[1] = e2[1] = e1[1] - 1
            else:
                if ra == rb:
                    write("YES\n")
                    continue
                lb += 1
                que = deque([ra])
                used[ra] = lb
                found = False
                while que:
                    v = que.popleft()
                    for w, d in G[v]:
                        if d and used[w] != lb:
                            if w == rb:
                                found = True
                                que.clear()
                                break
                            used[w] = lb
                            que.append(w)
                write("YES\n" if found else "NO\n")

solve()