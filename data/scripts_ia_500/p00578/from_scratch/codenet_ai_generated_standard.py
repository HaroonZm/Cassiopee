import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

height_with_index = sorted(((h, i) for i, h in enumerate(A)), reverse=True)
parent = [-1] * N

def find(x):
    while parent[x] >= 0:
        x = parent[x]
    return x

def union(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return False
    if parent[x] > parent[y]:
        x, y = y, x
    parent[x] += parent[y]
    parent[y] = x
    return True

added = [False]*N
island_count = 0
max_island = 0

for h, i in height_with_index:
    added[i] = True
    island_count += 1
    for ni in (i-1, i+1):
        if 0 <= ni < N and added[ni]:
            if union(i, ni):
                island_count -= 1
    if island_count > max_island:
        max_island = island_count

print(max_island)