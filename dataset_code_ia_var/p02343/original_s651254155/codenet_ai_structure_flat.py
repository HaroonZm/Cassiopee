import sys

n, q = map(int, input().split())

link = [i for i in range(n)]
size = [1 for _ in range(n)]

def find(x):
    while link[x] != x:
        link[x] = link[link[x]]
        x = link[x]
    return x

for _ in range(q):
    com, x, y = map(int, input().split())
    if com == 0:
        rx = find(x)
        ry = find(y)
        if rx == ry:
            continue
        if size[rx] < size[ry]:
            rx, ry = ry, rx
        link[ry] = rx
        size[rx] += size[ry]
    else:
        print(1 if find(x) == find(y) else 0)