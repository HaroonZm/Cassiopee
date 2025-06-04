import sys

# Lire largeur et hauteur
w, h = map(int, input().split())

# Lire la carte
mp = []
for i in range(h):
    row = input()
    mp.append(row)

# Initialisation des variables
springs = []
tile_cnt = 0
for y in range(h):
    for x in range(w):
        c = mp[y][x]
        if c == "*":
            springs.append((x, y))
        if c == "g":
            gx, gy = x, y
        if c == "s":
            sx, sy = x, y
            tile_cnt += 1
        if c == ".":
            tile_cnt += 1

# Déplacements possibles (droite, haut, gauche, bas)
vec = [(1, 0), (0, -1), (-1, 0), (0, 1)]

INF = 10**10

# BFS depuis la case 'g'
g_dist = []
for i in range(h):
    g_dist.append([INF] * w)
from collections import deque
q = deque()
q.append((0, gx, gy))
g_dist[gy][gx] = 0
while q:
    score, x, y = q.popleft()
    for dx, dy in vec:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < w and 0 <= ny < h:
            if mp[ny][nx] == "." or mp[ny][nx] == "s":
                if g_dist[ny][nx] == INF:
                    g_dist[ny][nx] = score + 1
                    q.append((score + 1, nx, ny))

# BFS depuis les 'springs'
s_dist = []
for i in range(h):
    s_dist.append([INF] * w)
q = deque()
for x, y in springs:
    s_dist[y][x] = 0
    q.append((0, x, y))
while q:
    score, x, y = q.popleft()
    for dx, dy in vec:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < w and 0 <= ny < h:
            if mp[ny][nx] == "." or mp[ny][nx] == "s":
                if s_dist[ny][nx] == INF:
                    s_dist[ny][nx] = score + 1
                    q.append((score + 1, nx, ny))

# Calcul des différences de distances et tri
sorted_tiles = []
for y in range(h):
    for x in range(w):
        if mp[y][x] == "." or mp[y][x] == "s":
            if g_dist[y][x] != INF:
                key = g_dist[y][x] - s_dist[y][x]
            else:
                key = INF
            sorted_tiles.append((key, x, y))
sorted_tiles.sort()

acc_g = 0
acc_s = 0
acc_t = 0
acc_g_dic = {}
acc_s_dic = {}
acc_t_dic = {}
keys = set()
for key, x, y in sorted_tiles:
    acc_g += g_dist[y][x]
    acc_s += s_dist[y][x]
    acc_t += 1
    acc_g_dic[key] = acc_g
    acc_s_dic[key] = acc_s
    acc_t_dic[key] = acc_t
    keys.add(key)

keys = list(keys)
keys.sort()
length = len(keys)
found = False
for i in range(length - 1):
    key = keys[i]
    next_key = keys[i + 1]
    # Moyenne pondérée
    E = (acc_g_dic[key] + acc_s - acc_s_dic[key]) / acc_t_dic[key]
    if key <= E < next_key:
        print(min(g_dist[sy][sx], s_dist[sy][sx] + E))
        found = True
        break

if not found:
    print(g_dist[sy][sx])