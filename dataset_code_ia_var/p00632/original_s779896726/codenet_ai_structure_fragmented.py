from collections import deque

def read_dimensions():
    return map(int, input().split())

def mp_row(w):
    return list("X" + input() + "X")

def read_map(h, w):
    mp = []
    for _ in range(h):
        mp.append(mp_row(w))
    return mp

def add_borders(mp, h, w):
    border = ["X"] * (w + 2)
    mp.insert(0, border)
    mp.append(border[:])
    return mp

def find_positions(mp, h, w):
    ax = ay = bx = by = None
    for y in range(h + 2):
        for x in range(w + 2):
            if mp[y][x] == "A":
                ax, ay = x, y
                mp[y][x] = "."
            elif mp[y][x] == "B":
                bx, by = x, y
                mp[y][x] = "."
    return ax, ay, bx, by

def create_distance_map(h, w, INF):
    return [[INF] * (w + 2) for _ in range(h + 2)]

def possible_neighbors(x, y):
    return [(x + 1, y), (x, y - 1), (x - 1, y), (x, y + 1)]

def bfs(mp, dist_mp, ax, ay, h, w, INF):
    que = deque()
    que.append((0, ax, ay))
    vecs = [(1,0), (0,-1), (-1,0), (0,1)]
    last_d = 0
    while que:
        d, x, y = que.popleft()
        last_d = d
        for dx, dy in vecs:
            nx, ny = x + dx, y + dy
            if mp[ny][nx] == "." and dist_mp[ny][nx] == INF:
                que.append((d + 1, nx, ny))
                dist_mp[ny][nx] = d + 1
    return last_d

def read_pattern():
    return input()

def move_possible(mp, by, bx, c):
    if c == "8" and mp[by - 1][bx] != "X":
        return by - 1, bx
    if c == "6" and mp[by][bx + 1] != "X":
        return by, bx + 1
    if c == "4" and mp[by][bx - 1] != "X":
        return by, bx - 1
    if c == "2" and mp[by + 1][bx] != "X":
        return by + 1, bx
    return by, bx

def can_escape(dist_mp, by, bx, t):
    return t >= dist_mp[by][bx]

def print_result(t, by, bx):
    print(t, by - 1, bx - 1)

def print_impossible():
    print("impossible")

def update_dict(dic, t, length, bx, by):
    key = (t % length, bx, by)
    if key in dic:
        return False
    dic[key] = True
    return True

def simulate_escape(mp, pattern, dist_mp, bx, by, limit):
    t = 0
    dic = {}
    length = len(pattern)
    while True:
        if can_escape(dist_mp, by, bx, t):
            print_result(t, by, bx)
            return
        if t > limit:
            if not update_dict(dic, t, length, bx, by):
                print_impossible()
                return
        c = pattern[t % length]
        if c != "5":
            by, bx = move_possible(mp, by, bx, c)
        t += 1
    print_impossible()

def process_case(h, w):
    mp = read_map(h, w)
    mp = add_borders(mp, h, w)
    ax, ay, bx, by = find_positions(mp, h, w)
    INF = 1000
    dist_mp = create_distance_map(h, w, INF)
    dist_mp[ay][ax] = 0
    limit = bfs(mp, dist_mp, ax, ay, h, w, INF)
    pattern = read_pattern()
    simulate_escape(mp, pattern, dist_mp, bx, by, limit)

def main_loop():
    while True:
        h, w = read_dimensions()
        if h == 0:
            break
        process_case(h, w)

main_loop()