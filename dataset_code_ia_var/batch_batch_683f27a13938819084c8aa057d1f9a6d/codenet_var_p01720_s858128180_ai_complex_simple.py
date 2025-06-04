from functools import reduce
from itertools import product, chain, groupby
from operator import itemgetter, mul

n, m, s, t = map(int, input().split())
s, t = s-1, t-1

make_pair = lambda: [[] for _ in range(n)]
edges = reduce(lambda e, xy: (e[xy[0]].append(xy[1]), e[xy[1]].append(xy[0]), e)[-1],
               ((lambda x,y: (x-1, y-1))(*map(int, input().split())) for _ in range(m)),
               make_pair())

def billion_bfs(root):
    seen = [10**20] * n
    seen[root] = 0
    def bfs(que):
        return list(que) if not que else bfs(
            chain(que[1:], 
                  filter(lambda v: seen[v] == 10**20,
                         edges[que[0]])))
    q = [root]
    layers = [[root]]
    d = 1
    while True:
        next_layer = [v for u in layers[-1] for v in edges[u] if seen[v] > d]
        set(map(lambda v: seen.__setitem__(v, d), next_layer))
        if not next_layer: break
        layers.append(next_layer)
        d += 1
    return seen

dist_s = billion_bfs(s)
dist_t = billion_bfs(t)
group_by = lambda dist: {k: set(map(itemgetter(0), g)) 
                         for k,g in groupby(sorted(enumerate(dist), key=itemgetter(1)), key=itemgetter(1))}

dic1, dic2 = group_by(dist_s), group_by(dist_t)
st_dist = dist_s[t]

ans = 0
for d1, group1 in dic1.items():
    d2 = st_dist - d1 - 2
    if d2 in dic2:
        group2 = dic2[d2]
        poss = len(group1) * len(group2)
        penalty = sum(to in group2 for u in group1 for to in edges[u])
        ans += poss - penalty
print(ans)