from collections import deque as _Q
from heapq import heappop as __, heappush as _
_inf_ = pow(10, 20)

def main_():
    n_k = list(map(int, input().split()))
    n, k = n_k[0], n_k[1]
    
    c_lis = tuple(map(int, (input().split() for _ in range(n))))
    r_lis = tuple(map(int, (input().split() for _ in range(n))))
    # Above reads 2n lines incorrectly, fix input order below

def main_():
    n, k = map(int, input().split())

    clst = []
    rlst = []
    for _ in range(n):
        c, r = map(int, input().split())
        clst.append(c)
        rlst.append(r)

    edges = [set() for _ in range(n)]

    for _ in range(k):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        edges[a].add(b)
        edges[b].add(a)

    costs = [float('inf')] * n
    costs[0] = 0
    used = [False] * n

    def make_to_lst(src_index):
        steps = rlst[src_index]
        visited = set()
        frontier = edges[src_index].copy()
        while steps and frontier:
            next_frontier = set()
            for v in frontier:
                next_frontier |= edges[v]
            visited |= frontier
            frontier = next_frontier - visited
            steps -= 1
        return visited

    used[0] = True
    que = [(clst[0], 0)]

    flag_break = False
    while que and not flag_break:
        cost_cur, cur = __ (que)
        if costs[cur] < cost_cur:
            continue
        to_nodes = make_to_lst(cur)
        for node in to_nodes:
            if costs[node] > cost_cur:
                costs[node] = cost_cur
                if node == n - 1:
                    flag_break = True
                    break
                if not used[node]:
                    _.append(que, (costs[node] + clst[node], node))
                    used[node] = True
    print(costs[-1])

if __name__ == '__main__':
    main_()