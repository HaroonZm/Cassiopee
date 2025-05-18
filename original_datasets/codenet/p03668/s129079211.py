import sys

n = int(sys.stdin.buffer.readline())
mp = map(int, sys.stdin.buffer.read().split())
links = [set() for _ in range(n)]
for x, y in zip(mp, mp):
    x -= 1
    y -= 1
    links[x].add(y)
    links[y].add(x)

stack = [(0, -2)]
grundy = [0] * n
while stack:
    v, p = stack.pop()
    if p == -1:
        g = 0
        # second visit (aggregate children and calculate self grundy)
        for u in links[v]:
            g ^= grundy[u] + 1
        grundy[v] = g
    else:
        # first visit (stack children and remove parent)
        links[v].discard(p)
        stack.append((v, -1))
        for u in links[v]:
            stack.append((u, v))

if grundy[0] == 0:
    print('Bob')
else:
    print('Alice')