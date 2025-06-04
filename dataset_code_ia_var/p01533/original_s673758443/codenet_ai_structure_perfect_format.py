from itertools import permutations
from collections import deque

w, h = map(int, input().split())
mp = ["X" * (w + 4)] * 2 + ["XX" + input() + "XX" for _ in range(h)] + ["X" * (w + 4)] * 2
m_lst = []
holes = []
for y in range(2, h + 2):
    for x in range(2, w + 2):
        if mp[y][x] == "S":
            sx, sy = x, y
        if mp[y][x] == "G":
            gx, gy = x, y
        if mp[y][x] == "M":
            m_lst.append((x, y))
        if mp[y][x] == "#":
            holes.append((x, y))

move_costs = [[1] * (w + 4) for _ in range(h + 4)]
for x, y in holes:
    for ny in range(y - 2, y + 3):
        for nx in range(x - 2, x + 3):
            move_costs[ny][nx] = max(2, move_costs[ny][nx])
    for ny in range(y - 1, y + 2):
        for nx in range(x - 1, x + 2):
            move_costs[ny][nx] = 3

def shortest(x1, y1):
    INF = 10 ** 20
    vec = ((1, 0), (0, -1), (-1, 0), (0, 1))
    costs = [[INF] * (w + 4) for _ in range(h + 4)]
    costs[y1][x1] = 0
    que = deque()
    que.append((0, x1, y1))
    while que:
        score, x, y = que.popleft()
        new_score = score + move_costs[y][x]
        for dx, dy in vec:
            nx, ny = x + dx, y + dy
            if mp[ny][nx] in {"S", "G", ".", "M"} and new_score < costs[ny][nx]:
                costs[ny][nx] = new_score
                que.append((new_score, nx, ny))
    return costs

edges = []
for x, y in m_lst:
    costs = shortest(x, y)
    edge = []
    for x2, y2 in m_lst:
        edge.append(costs[y2][x2])
    edge.append(costs[gy][gx])
    edges.append(edge)

start_cost = shortest(sx, sy)
goal_cost = shortest(gx, gy)
ans = 10 ** 20
for t in permutations(range(len(edges)), len(edges)):
    lst = list(t)
    score = 0
    for i in range(len(edges) - 1):
        score += edges[lst[i]][lst[i + 1]]
    xs, ys = m_lst[lst[0]]
    xf, yf = m_lst[lst[-1]]
    score += start_cost[ys][xs]
    score += edges[lst[-1]][-1]
    ans = min(ans, score)

print(ans)