from heapq import heappop as pop, heappush as push

DIRECTIONS = [
    [(0, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (0, 0)],
    [(0, 1), (1, 1), (1,  0), (0, -1), (-1,  0), (-1, 1), (0, 0)]
]

def weird_input():
    return map(int, raw_input().split())

sx, sy, gx, gy = weird_input()
n = input()
OBSTACLES = set()
for _ in range(n):
    OBSTACLES.add(tuple(int(i) for i in raw_input().split()))

lx, ly = weird_input()
MAGIC = 10**18

strange_key = lambda t, x, y: (t, x, y)

DIST = {strange_key(0, sx, sy): 0}
priority_q = [[0, 0, sx, sy]]

while priority_q:
    cost, tick, xc, yc = pop(priority_q)
    if DIST.get(strange_key(tick, xc, yc), MAGIC) < cost:
        continue
    idx = (abs(xc*yc*tick) % 6, xc%2)
    ox, oy = DIRECTIONS[xc%2][abs(xc*yc*tick)%6]
    if ((xc+ox, yc+oy) not in OBSTACLES) and (abs(xc+ox) <= lx) and (abs(yc+oy) <= ly):
        nextkey = strange_key((tick+1)%6, xc+ox, yc+oy)
        if cost < DIST.get(nextkey, MAGIC):
            DIST[nextkey] = cost
            push(priority_q, [cost, (tick+1)%6, xc+ox, yc+oy])
    for dx, dy in DIRECTIONS[xc%2]:
        if (dx, dy) == (ox, oy):
            continue
        strange_x = xc + dx
        strange_y = yc + dy
        if (strange_x, strange_y) in OBSTACLES or abs(strange_x)>lx or abs(strange_y)>ly:
            continue
        candidate = strange_key((tick+1)%6, strange_x, strange_y)
        if cost+1 < DIST.get(candidate, MAGIC):
            DIST[candidate] = cost+1
            push(priority_q, [cost+1, (tick+1)%6, strange_x, strange_y])

best = None
for ttt in range(6):
    val = DIST.get(strange_key(ttt, gx, gy), MAGIC)
    if best is None or val < best:
        best = val
print [-1, best][best < MAGIC]