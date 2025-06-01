from heapq import heappush, heappop

h, w = map(int, input().split())
# Lecture et padding de la carte avec -1
mp = [[-1] * (w + 2)] + [[-1] + [int(c) if c.isdigit() else 0 if c == '.' else -1 for c in input()] + [-1] for _ in range(h)] + [[-1] * (w + 2)]

# Initialisation de la file de priorité avec les positions où la valeur est 0 ('.')
que = [(0, x, y) for y in range(1, h + 1) for x in range(1, w + 1) if mp[y][x] == 0]
# Transforme la liste en tas en place
import heapq
heapq.heapify(que)

# Directions 8-voisines
vec = ((0,1),(0,-1),(1,1),(1,0),(1,-1),(-1,1),(-1,0),(-1,-1))

turn = 0
while que:
    turn, x, y = heappop(que)
    for dx, dy in vec:
        nx, ny = x + dx, y + dy
        val = mp[ny][nx]
        if val and val > 0:
            mp[ny][nx] = val - 1
            if mp[ny][nx] == 0:
                heappush(que, (turn + 1, nx, ny))

print(turn)