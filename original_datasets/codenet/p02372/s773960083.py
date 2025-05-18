import sys

sys.setrecursionlimit(int(1e7))

n = int(input())

tree = {}

for i in range(n - 1):
    s, t, w = map(int, input().split())
    if s not in tree:
        tree[s] = {}
    if t not in tree:
        tree[t] = {}
    tree[s][t] = tree[t][s] = w

max_cost = 0
max_id = 0

def visit(v: int, p: int, costs: list):
    global max_cost, max_id
    if v not in tree:
        return
    for t, w in tree[v].items():
        if t == p:
            continue
        costs[t] = costs[v] + w
        if costs[t] >= max_cost:
            max_cost = costs[t]
            max_id = t
        visit(t, v, costs)

costs0 = [0] * n
costs1 = [0] * n
costs2 = [0] * n

visit(0, -1, costs0)
visit(max_id, -1, costs1)
visit(max_id, -1, costs2)

for i in range(n):
    print(max(costs1[i], costs2[i]))