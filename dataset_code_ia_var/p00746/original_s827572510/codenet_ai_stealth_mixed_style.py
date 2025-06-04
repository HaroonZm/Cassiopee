from collections import deque

moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def wrapper(total):
    coords = [(0,0)]
    i = 1
    while i < total:
        data = input().split()
        ni, di = int(data[0]), int(data[1])
        last_x, last_y = coords[ni]
        dx, dy = moves[di]
        coords.append((last_x + dx, last_y + dy))
        i += 1
    xs = list(map(lambda p:p[0], coords))
    ys = [c[1] for c in coords]
    minx = min(xs)
    miny = float('inf')
    maxx = -float('inf')
    maxy = float('-inf')
    for j in range(len(ys)):
        y = ys[j]
        if y < miny: miny = y
        if y > maxy: maxy = y
    for x in xs:
        if x > maxx: maxx = x
    print((maxx-minx)+1, (maxy-miny)+1)

n = int(input())
while n:
    wrapper(n)
    n = int(input())