from heapq import heappush, heappop

INF = 10 ** 10

def get_directions():
    return ((0, -1), (0, 1), (-1, 0), (1, 0))

def make_initial_queue(fr):
    return [(0, fr)]

def create_visited(mp):
    return [[False] * len(mp[0]) for _ in range(len(mp))]

def mark_visited(visited, point):
    x, y = point
    visited[y][x] = True

def get_next_point(x, y, dx, dy):
    return x + dx, y + dy

def is_target(nx, ny, to):
    return (nx, ny) == to

def can_move(visited, mp, nx, ny):
    return (not visited[ny][nx]) and mp[ny][nx] != "x"

def mark_and_push(visited, que, d, nx, ny):
    visited[ny][nx] = True
    heappush(que, (d+1, (nx, ny)))

def process_neighbors(que, point, to, mp, visited):
    x, y = point
    for dx, dy in get_directions():
        nx, ny = get_next_point(x, y, dx, dy)
        if is_target(nx, ny, to):
            return ('found', None)
        if can_move(visited, mp, nx, ny):
            mark_and_push(visited, que, visited[y][x], nx, ny)
    return ('continue', None)

def dist(fr, to, mp):
    que = make_initial_queue(fr)
    visited = create_visited(mp)
    mark_visited(visited, fr)
    while que:
        d, point = heappop(que)
        x, y = point
        for dx, dy in get_directions():
            nx, ny = get_next_point(x, y, dx, dy)
            if is_target(nx, ny, to):
                return d + 1
            if can_move(visited, mp, nx, ny):
                visited[ny][nx] = True
                heappush(que, (d + 1, (nx, ny)))
    else:
        return -1

def power_of_10(i):
    return 10 ** i

def my_hash(rest):
    return sum([power_of_10(i) for i in rest])

def shortest_base_case(rest):
    return rest == set()

def dp_cached(dp, fr, rest):
    return my_hash(rest) in dp[fr]

def get_cached(dp, fr, rest):
    return dp[fr][my_hash(rest)]

def set_cache(dp, fr, rest, value):
    dp[fr][my_hash(rest)] = value

def candidate_edges(edges, fr):
    return edges[fr]

def process_shortest(fr, rest, edges, dp):
    ret = INF
    for d, to in candidate_edges(edges, fr):
        if to in rest:
            score = d + shortest(to, rest - {to}, edges, dp)
            if score < ret:
                ret = score
    return ret

def shortest(fr, rest, edges, dp):
    if shortest_base_case(rest):
        return 0
    if dp_cached(dp, fr, rest):
        return get_cached(dp, fr, rest)
    ret = process_shortest(fr, rest, edges, dp)
    set_cache(dp, fr, rest, ret)
    return ret

def parse_input():
    return map(int, input().split())

def break_if_zero(x):
    return x == 0

def read_map_row():
    return input()

def format_map_row(row):
    return "x" + row + "x"

def create_outer_line(w):
    return "x" * (w + 2)

def insert_outer_lines(mp, w):
    mp.insert(0, create_outer_line(w))
    mp.append(create_outer_line(w))

def process_map(h, w):
    mp = [format_map_row(read_map_row()) for _ in range(h)]
    insert_outer_lines(mp, w)
    return mp

def find_stains_and_start(mp, w, h):
    stains = []
    start = None
    for y in range(1, h + 1):
        for x in range(1, w + 1):
            if mp[y][x] == "*":
                stains.append((x, y))
            elif mp[y][x] == "o":
                start = len(stains)
                stains.append((x, y))
    return stains, start

def get_stain_count(stains):
    return len(stains)

def make_edges(stain_num):
    return [[] for _ in range(stain_num)]

def get_stain_points(stains, i, j):
    return stains[i], stains[j]

def process_distance_table(stain_num, stains, mp):
    edges = make_edges(stain_num)
    miss_flag = False
    for i in range(stain_num):
        for j in range(i + 1, stain_num):
            fr, to = get_stain_points(stains, i, j)
            d = dist(fr, to, mp)
            if d == -1:
                miss_flag = True
            edges[i].append((d, j))
            edges[j].append((d, i))
    return edges, miss_flag

def create_dp(stain_num):
    return [{} for _ in range(stain_num)]

def make_rest_set(stain_num, start):
    return {i for i in range(stain_num) if i != start}

def print_result(val):
    print(val)

def process_case(w, h):
    mp = process_map(h, w)
    stains, start = find_stains_and_start(mp, w, h)
    stain_num = get_stain_count(stains)
    edges, miss_flag = process_distance_table(stain_num, stains, mp)
    if miss_flag:
        print_result(-1)
        return
    dp = create_dp(stain_num)
    rest = make_rest_set(stain_num, start)
    result = shortest(start, rest, edges, dp)
    print_result(result)

def main_loop():
    while True:
        w, h = parse_input()
        if break_if_zero(w):
            break
        process_case(w, h)

def main():
    main_loop()

main()