import sys
from heapq import heappush, heappop
sys.setrecursionlimit(100000)
INF = 10 ** 10

def get_directions():
    return ((0, -1), (0, 1), (-1, 0), (1, 0))

def initialize_visited(width, height):
    return [[False] * width for _ in range(height)]

def mark_visited(visited, x, y):
    visited[y][x] = True

def is_valid_cell(mp, x, y):
    return mp[y][x] != "x"

def is_destination(nx, ny, to):
    return (nx, ny) == to

def push_queue(que, d, nx, ny):
    heappush(que, (d, (nx, ny)))

def pop_queue(que):
    return heappop(que)

def handle_while_empty():
    return -1

def generate_neighbors(point):
    x, y = point
    neighbors = []
    for dx, dy in get_directions():
        nx, ny = x + dx, y + dy
        neighbors.append((nx, ny))
    return neighbors

def in_bounds(mp, nx, ny):
    return 0 <= ny < len(mp) and 0 <= nx < len(mp[0])

def dist(fr, to, mp):
    que = []
    heappush(que, (0, fr))
    visited = initialize_visited(len(mp[0]), len(mp))
    mark_visited(visited, fr[0], fr[1])
    while que:
        d, point = pop_queue(que)
        x, y = point
        for dx, dy in get_directions():
            nx, ny = x + dx, y + dy
            if is_destination(nx, ny, to):
                return d + 1
            if in_bounds(mp, nx, ny) and not visited[ny][nx] and is_valid_cell(mp, nx, ny):
                mark_visited(visited, nx, ny)
                push_queue(que, d + 1, nx, ny)
    return handle_while_empty()

def my_hash(rest):
    return sum([10 ** i for i in rest])

def is_dp_key_present(fr, rest, dp):
    return my_hash(rest) in dp[fr]

def find_shortest(am, bm):
    if am < bm:
        return am
    else:
        return bm

def update_dp(fr, rest, ret, dp):
    dp[fr][my_hash(rest)] = ret

def neighbors_edges(fr, edges):
    return edges[fr]

def shortest_core(fr, rest, edges, dp):
    ret = INF
    for d, to in neighbors_edges(fr, edges):
        if to in rest:
            score = d + shortest(to, rest - {to}, edges, dp)
            ret = find_shortest(score, ret)
    return ret

def handle_base_case():
    return 0

def shortest(fr, rest, edges, dp):
    if rest == set():
        return handle_base_case()
    if is_dp_key_present(fr, rest, dp):
        return dp[fr][my_hash(rest)]
    ret = shortest_core(fr, rest, edges, dp)
    update_dp(fr, rest, ret, dp)
    return ret

def read_grid_dimensions():
    return map(int, input().split())

def is_end_case(w):
    return w == 0

def process_input_line():
    return input()

def build_map(w, h):
    mp = ["x" + process_input_line() + "x" for _ in range(h)]
    mp.insert(0, "x" * (w + 2))
    mp.append("x" * (w + 2))
    return mp

def get_stains_and_start(mp, w, h):
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

def create_edges_and_distances(stains, mp):
    stain_num = len(stains)
    edges = [[] for _ in range(stain_num)]
    D = [[None] * stain_num for _ in range(stain_num)]
    for i in range(stain_num):
        D[i][i] = 0
    miss_flag = [False]
    fill_edges(stain_num, stains, mp, edges, D, miss_flag)
    return edges, D, miss_flag[0]

def fill_edges(stain_num, stains, mp, edges, D, miss_flag):
    for i in range(stain_num):
        for j in range(i + 1, stain_num):
            fr = stains[i]
            to = stains[j]
            d = dist(fr, to, mp)
            if d == -1:
                miss_flag[0] = True
            edges[i].append((d, j))
            edges[j].append((d, i))
            D[i][j] = d
            D[j][i] = d

def print_fail():
    print(-1)

def remove_start_from_stains(stain_num, start):
    return {i for i in range(stain_num) if i != start}

def create_dp_table():
    return [{} for _ in range(10)]

def print_result(result):
    print(result)

def main_one_iteration():
    w, h = read_grid_dimensions()
    if is_end_case(w):
        return False
    mp = build_map(w, h)
    stains, start = get_stains_and_start(mp, w, h)
    stain_num = len(stains)
    edges, D, miss_flag = create_edges_and_distances(stains, mp)
    if miss_flag:
        print_fail()
        return True
    dp = create_dp_table()
    result = shortest(start, remove_start_from_stains(stain_num, start), edges, dp)
    print_result(result)
    return True

def main():
    while True:
        should_continue = main_one_iteration()
        if not should_continue:
            break

main()