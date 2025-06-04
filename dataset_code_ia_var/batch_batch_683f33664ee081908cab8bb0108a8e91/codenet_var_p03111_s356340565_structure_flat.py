import sys
sys.setrecursionlimit(1000000000)
INF = 10**9
n, a, b, c = map(int, input().split())
l = [int(input()) for i in range(n)]
stack = []
stack.append((0, 0, 0, 0, 0))
best = INF
visited = {}
while stack:
    i, x, y, z, m = stack.pop()
    key = (i, x, y, z, m)
    if key in visited:
        continue
    visited[key] = True
    if i == n:
        if x > 0 and y > 0 and z > 0:
            cost = abs(x - a) + abs(y - b) + abs(z - c) + m
            if cost < best:
                best = cost
        continue
    v = l[i]
    # assign to x
    if x == 0:
        stack.append((i + 1, v, y, z, m))
    else:
        stack.append((i + 1, x + v, y, z, m + 10))
    # assign to y
    if y == 0:
        stack.append((i + 1, x, v, z, m))
    else:
        stack.append((i + 1, x, y + v, z, m + 10))
    # assign to z
    if z == 0:
        stack.append((i + 1, x, y, v, m))
    else:
        stack.append((i + 1, x, y, z + v, m + 10))
    # skip
    stack.append((i + 1, x, y, z, m))
print(best)