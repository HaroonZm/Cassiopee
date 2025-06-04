from heapq import heappush, heappop

INF = 10 ** 10

def get_directions():
    return ((0, -1), (0, 1), (-1, 0), (1, 0))

def prepare_queue(fr):
    que = []
    heappush(que, (0, fr))
    return que

def create_visited(mp):
    return [[False] * len(mp[0]) for _ in range(len(mp))]

def mark_visited(visited, point):
    x, y = point
    visited[y][x] = True

def get_next_point(x, y, dx, dy):
    return x + dx, y + dy

def is_goal(nx, ny, to):
    return (nx, ny) == to

def is_within_bounds(mp, nx, ny):
    return 0 <= ny < len(mp) and 0 <= nx < len(mp[0])

def is_not_visited(visited, nx, ny):
    return not visited[ny][nx]

def is_not_obstacle(mp, nx, ny):
    return mp[ny][nx] != "x"

def handle_goal(d):
    return d + 1

def mark_and_push(visited, mp, nx, ny, d, que):
    visited[ny][nx] = True
    heappush(que, (d + 1, (nx, ny)))

def dist(fr, to, mp):
    que = prepare_queue(fr)
    visited = create_visited(mp)
    mark_visited(visited, fr)
    direct = get_directions()
    while que:
        d, point = heappop(que)
        x, y = point
        for dx, dy in direct:
            nx, ny = get_next_point(x, y, dx, dy)
            if not is_within_bounds(mp, nx, ny):
                continue
            if is_goal(nx, ny, to):
                return handle_goal(d)
            if is_not_visited(visited, nx, ny) and is_not_obstacle(mp, nx, ny):
                mark_and_push(visited, mp, nx, ny, d, que)
    return -1

def my_hash(rest):
    return compute_hash(rest)

def compute_hash(rest):
    ret = 0
    for i in rest:
        ret += 10 ** i
    return ret

def is_rest_empty(rest):
    return rest == set()

def is_h_in_dp(fr, h, dp):
    return h in dp[fr]

def update_ret_if_better(score, ret):
    return score if score < ret else ret

def store_in_dp(dp, fr, h, ret):
    dp[fr][h] = ret

def get_rest_minus_to(rest, to):
    return rest - {to}

def shortest(fr, rest, edges, dp):
    if is_rest_empty(rest):
        return 0
    h = my_hash(rest)
    if is_h_in_dp(fr, h, dp):
        return dp[fr][h]
    ret = INF
    for d, to in edges[fr]:
        if to in rest:
            score = d + shortest(to, get_rest_minus_to(rest, to), edges, dp)
            ret = update_ret_if_better(score, ret)
    store_in_dp(dp, fr, h, ret)
    return ret

def should_break_loop(w):
    return w == 0

def read_dimensions():
    return map(int, input().split())

def add_border_to_row(row):
    return "x" + row + "x"

def create_map(w, h):
    mp = []
    for _ in range(h):
        row = input()
        mp.append(add_border_to_row(row))
    mp.insert(0, "x" * (w + 2))
    mp.append("x" * (w + 2))
    return mp

def collect_stains(mp, w, h):
    stains = []
    start = -1
    for y in range(1, h + 1):
        for x in range(1, w + 1):
            cell = mp[y][x]
            if cell == "*":
                stains.append((x, y))
            elif cell == "o":
                start = len(stains)
                stains.append((x, y))
    return stains, start

def create_edges(stains, mp):
    stain_num = len(stains)
    edges = [[] for _ in range(stain_num)]
    miss_flag = False
    for i in range(stain_num):
        for j in range(i + 1, stain_num):
            fr = stains[i]
            to = stains[j]
            d = dist(fr, to, mp)
            if d == -1:
                miss_flag = True
            edges[i].append((d, j))
            edges[j].append((d, i))
    return edges, miss_flag

def print_and_continue(val):
    print(val)

def run_algorithm(start, stains, edges):
    dp = [{} for _ in range(len(stains))]
    needed_set = get_needed_set(len(stains), start)
    print(shortest(start, needed_set, edges, dp))

def get_needed_set(stain_num, start):
    return {i for i in range(stain_num) if i != start}

def process_one_case():
    w, h = read_dimensions()
    if should_break_loop(w):
        return False
    mp = create_map(w, h)
    stains, start = collect_stains(mp, w, h)
    edges, miss_flag = create_edges(stains, mp)
    if miss_flag:
        print_and_continue(-1)
        return True
    run_algorithm(start, stains, edges)
    return True

def main_loop():
    while True:
        if not process_one_case():
            break

def main():
    main_loop()

main()