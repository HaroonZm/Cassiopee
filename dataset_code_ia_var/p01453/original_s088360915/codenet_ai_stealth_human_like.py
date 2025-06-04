from collections import deque

# On prend la taille, classique
w, h = map(int, input().split())
mp = []
for _ in range(h):
    mp.append(input())

springs = []
tile_cnt = 0
# repère les positions g, s, * et compte les tuiles
for y in range(h):
    for x in range(w):
        cell = mp[y][x]
        if cell == '*':
            springs.append((x, y))
        if cell == 's':
            sx, sy = x, y
            tile_cnt += 1
        elif cell == 'g':
            gx, gy = x, y
        elif cell == '.':
            tile_cnt += 1
        # il me semble qu'on pourrait regrouper le count, mais bon

vec = [(1, 0), (0, -1), (-1, 0), (0, 1)]
INF = 10**10

# distance depuis g (but? goal?)
g_dist = [[INF]*w for _ in range(h)]
queue = deque()
g_dist[gy][gx] = 0
queue.append((0, gx, gy))
while queue:
    sc, px, py = queue.popleft()
    for dx, dy in vec:
        nx, ny = px + dx, py + dy
        if 0 <= nx < w and 0 <= ny < h:
            if mp[ny][nx] in ('.', 's') and g_dist[ny][nx] == INF:
                g_dist[ny][nx] = sc + 1
                queue.append((sc+1, nx, ny))

# Depuis chaque ressort, pareil
s_dist = [[INF]*w for _ in range(h)]
queue = deque()
for xx, yy in springs:
    s_dist[yy][xx] = 0
    queue.append((0, xx, yy))
while queue:
    val, px, py = queue.popleft()
    for dx, dy in vec:
        nx, ny = px + dx, py + dy
        if 0 <= nx < w and 0 <= ny < h:
            if mp[ny][nx] in ('.', 's') and s_dist[ny][nx] == INF:
                s_dist[ny][nx] = val + 1
                queue.append((val+1, nx, ny))

# ça va être trié par la différence entre les deux distances... j'espère que c'est optimal
sorted_tiles = []
for y in range(h):
    for x in range(w):
        if mp[y][x] in ('.', 's'):
            diff = g_dist[y][x] - s_dist[y][x] if g_dist[y][x] != INF else INF
            sorted_tiles.append((diff, x, y))
sorted_tiles.sort()

acc_g = 0
acc_s = 0
acc_t = 0
acc_g_dic = {}
acc_s_dic = {}
acc_t_dic = {}
keys = set()
# on calcule tout ça d'un coup, honnêtement un peu moche mais bon
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

# la logique principale pour afficher le résultat, mais je ne l'explique pas trop
nkeys = len(keys)
found = False
for i in range(nkeys-1):
    k = keys[i]
    k_next = keys[i+1]
    if acc_t_dic[k] == 0: continue  # pour éviter une division par zéro hasardeuse
    E = (acc_g_dic[k] + acc_s - acc_s_dic[k]) / acc_t_dic[k]
    if k <= E < k_next:
        print(min(g_dist[sy][sx], s_dist[sy][sx] + E))
        found = True
        break
if not found:
    print(g_dist[sy][sx])
# il faudrait vérifier les cas limites peut-être, mais ça marche comme ça...