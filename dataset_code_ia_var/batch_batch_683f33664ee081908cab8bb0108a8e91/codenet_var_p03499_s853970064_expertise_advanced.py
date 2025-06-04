from functools import lru_cache, reduce
from operator import mul
from collections import deque, defaultdict

mod = 10**9 + 7

@lru_cache(maxsize=None)
def pow2(x):
    return pow(2, x, mod)

n = int(input())
parents = list(map(int, input().split()))
tree = defaultdict(set)
for idx, p in enumerate(parents, 1):
    tree[p].add(idx)

levels = [{0}]
while True:
    nxt = set().union(*(tree[p] for p in levels[-1]))
    if not nxt:
        break
    levels.append(nxt)
levels = levels[::-1]
level_sizes = list(map(len, levels))

balls = [None] * (n + 1)
for lvl_nodes in levels:
    for node in lvl_nodes:
        children_nodes = tree[node]
        if children_nodes:
            if len(children_nodes) == 1:
                child = children_nodes.pop()
                bs = balls[child]
                bs.appendleft([1, 1, 0])
                balls[node] = bs
                tree[node].add(child)  # restore for further loops
            else:
                bss = [balls[c] for c in sorted(children_nodes, key=lambda x: len(balls[x]))]
                merged = bss[0]
                for bs in bss[1:]:
                    for v1, v2 in zip(merged, bs):
                        v2[2] = ((v1[1]+v1[2])*v2[1] + v1[2]*v2[0]) % mod
                        v2[1] = (v1[0]*v2[1] + v1[1]*v2[0]) % mod
                        v2[0] = v1[0]*v2[0] % mod
                    merged = bs
                for b in merged:
                    b[0] = (b[0]+b[2]) % mod
                    b[2] = 0
                merged.appendleft([1, 1, 0])
                balls[node] = merged
        else:
            balls[node] = deque([[1, 1, 0]])

level_sizes = level_sizes[::-1]
result = sum(b[1] * pow2(n-l+1) % mod for l, b in zip(level_sizes, balls[0])) % mod
print(result)