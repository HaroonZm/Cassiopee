import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N = int(input())
items = []
price_map = {}
for _ in range(N):
    a, x = input().split()
    x = int(x)
    items.append((a, x))
    price_map[a] = x

M = int(input())
parent = {}
rank = {}

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    if rank[x] < rank[y]:
        parent[x] = y
        min_price[y] = min(min_price[y], min_price[x])
    else:
        parent[y] = x
        min_price[x] = min(min_price[x], min_price[y])
        if rank[x] == rank[y]:
            rank[x] += 1

for a, _ in items:
    parent[a] = a
    rank[a] = 0

min_price = {a: x for a, x in items}

for _ in range(M):
    s, t = input().split()
    union(s, t)

ans = 0
for a, _ in items:
    ans += min_price[find(a)]
print(ans)