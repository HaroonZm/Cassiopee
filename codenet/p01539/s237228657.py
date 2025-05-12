from heapq import heappush, heappop
dd = [
    [(0, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (0, 0)],
    [(0, 1), (1, 1), (1,  0), (0, -1), (-1,  0), (-1, 1), (0, 0)]
]
sx, sy, gx, gy = map(int, raw_input().split())
n = input()
P = {tuple(map(int, raw_input().split())) for i in xrange(n)}
lx, ly = map(int, raw_input().split())

INF = 10**18

dist = {(0, sx, sy): 0}
que = [(0, 0, sx, sy)]
while que:
    co, t, x, y = heappop(que)
    if dist.get((t, x, y), INF) < co:
        continue
    ox, oy = dd[x%2][abs(x*y*t) % 6]
    if (x+ox, y+oy) not in P and abs(x+ox) <= lx and abs(y+oy) <= ly:
        if co < dist.get(((t+1)%6, x+ox, y+oy), INF):
            dist[(t+1)%6, x+ox, y+oy] = co
            heappush(que, (co, (t+1)%6, x+ox, y+oy))
    for dx, dy in dd[x%2]:
        if dx == ox and dy == oy:
            continue
        nx = x+dx; ny = y+dy
        if (nx, ny) in P or abs(nx)>lx or abs(ny)>ly:
            continue
        if co+1 < dist.get(((t+1)%6, nx, ny), INF):
            dist[(t+1)%6, nx, ny] = co+1
            heappush(que, (co+1, (t+1)%6, nx, ny))
v = min(dist.get((t, gx, gy), INF) for t in xrange(6))
print -1 if v == INF else v