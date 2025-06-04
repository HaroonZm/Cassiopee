from functools import reduce, lru_cache
from itertools import permutations
*N, = map(int, input().split())
used = set(filter(lambda x: x != -1, N))
domain = set(range(1, 10)).difference(used)
C = [1, 10, 1, 100, 10, 1, -100, -10, -1]
positions = [i for i, v in enumerate(N) if v == -1]
indices = [i for i in range(9)]

def solve():
    return int(sum(map(lambda i: C[i]*N[i], indices)) == 0)

def fancy_dfs(c, rest, history=[]):
    if rest == 0:
        return solve()
    if N[c] != -1:
        return fancy_dfs(c+1, rest, history)
    elements = tuple(domain - set(history))
    result = 0
    for idx in range(len(elements)):
        v = list(elements)[idx]
        N[c] = v
        result += fancy_dfs(c+1, rest-1, history+[v])
        N[c] = -1
    return result

print(fancy_dfs(0, len(domain)))