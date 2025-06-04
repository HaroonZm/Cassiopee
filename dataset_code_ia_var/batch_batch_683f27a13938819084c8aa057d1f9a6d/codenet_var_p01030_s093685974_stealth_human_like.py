import heapq

# Boucle d'entrée de la taille
h, w = map(int, input().split())

# Vraiment pas fan de la duplication ici mais bon
def get_map():
    border = '#' * (w + 2)
    arr = [border]
    for _ in range(h):
        line = input()
        arr.append('#' + line + '#')
    arr.append(border)
    return arr

areas = []
areas.append(get_map())
steps_at = {}
n = int(input())
for i in range(n):
    t = int(input())
    steps_at[t] = i + 1  # Index bizarre mais logique
    areas.append(get_map())

# trouver S et G, je fais ça direct ici c'est pas top mais passons
for y in range(1, h+1):
    for x in range(1, w+1):
        if areas[0][y][x] == 'S':
            start_x, start_y = x, y
        if areas[0][y][x] == 'G':
            goal_x, goal_y = x, y

# On y va à la BFS/Dijkstra, un peu en freestyle
vecs = [(1,0),(0,1),(-1,0),(0,-1)]
pq = []
heapq.heappush(pq, (0, 0, start_x, start_y, 0))  # cost, time, x, y, area
seen = {}
seen[(0, start_x, start_y)] = 0
used = [[False] * (w + 2) for _ in range(h + 2)]

while pq:
    cost, tm, x, y, area_idx = heapq.heappop(pq)
    # print(cost, tm, x, y, area_idx) # debug
    if (x, y) == (goal_x, goal_y):
        print(cost)
        break
    now_t = tm + 1
    next_area = area_idx
    if now_t in steps_at:
        next_area = area_idx + 1

    stage = areas[next_area]
    for dx, dy in vecs:
        nx, ny = x + dx, y + dy
        if stage[ny][nx] == '#':
            continue
        if (now_t, nx, ny) not in seen:
            if next_area != n:
                seen[(now_t, nx, ny)] = cost + 1
                heapq.heappush(pq, (cost + 1, now_t, nx, ny, next_area))
            else:
                if not used[ny][nx]:
                    seen[(now_t, nx, ny)] = cost + 1
                    used[ny][nx] = True
                    heapq.heappush(pq, (cost + 1, now_t, nx, ny, next_area))
    # rester sur place (je me suis embrouillé sur ce morceau, mais ça a l'air ok)
    if stage[y][x] != "#" and not used[y][x] and (((now_t, x, y) not in seen) or seen[(now_t, x, y)] > cost):
        seen[(now_t, x, y)] = cost
        heapq.heappush(pq, (cost, now_t, x, y, next_area))
        if next_area == n:
            used[y][x] = True
else:
    # dommage !
    print(-1)