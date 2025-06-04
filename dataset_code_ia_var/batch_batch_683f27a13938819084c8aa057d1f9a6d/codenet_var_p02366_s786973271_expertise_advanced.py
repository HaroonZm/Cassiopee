import sys
from collections import defaultdict
from itertools import count

sys.setrecursionlimit(10**7)

def run():
    V, E = map(int, input().split())
    if V == 1:
        return

    g = defaultdict(list)
    for _ in range(E):
        A, B = map(int, input().split())
        g[A].append(B)
        g[B].append(A)

    order = [0] * V
    art_points = set()
    c = count(1)

    def dfs(u, parent):
        order_u = order[u-1] = next(c)
        low_u = order_u
        child_count = 0
        is_art = False
        for v in g[u]:
            if v == parent:
                continue
            if not order[v-1]:
                child_count += 1
                low_v = dfs(v, u)
                if parent != -1 and low_v >= order_u:
                    is_art = True
                low_u = min(low_u, low_v)
            else:
                low_u = min(low_u, order[v-1])
        if (parent == -1 and child_count > 1) or (parent != -1 and is_art):
            art_points.add(u)
        return low_u

    dfs(1, -1)
    print(*sorted(art_points), sep='\n')

if __name__ == '__main__':
    run()