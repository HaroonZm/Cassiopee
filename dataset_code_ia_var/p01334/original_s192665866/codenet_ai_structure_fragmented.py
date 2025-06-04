def read_N():
    return int(raw_input())

def should_break(N):
    return N == 0

def read_field_line(N):
    return map(int, raw_input().split())

def create_empty_field(N):
    return [[(0, 0) for _ in xrange(N)] for _ in xrange(N)]

def fill_field_row(field, y, row_vals, N):
    for x in xrange(N):
        field[y][x] = (row_vals[2 * x + 1], row_vals[2 * x])

def build_field(N):
    field = create_empty_field(N)
    for y in xrange(N):
        line = read_field_line(N)
        fill_field_row(field, y, line, N)
    return field

def coord_tuple(y, x):
    return (y, x)

def already_visited(cur, vis):
    return cur in vis

def initialize_loop(cur):
    loop = set()
    loop.add(cur)
    return loop

def get_next_cur(cur, field):
    return field[cur[0]][cur[1]]

def update_vis_loop(vis, loop):
    vis = vis | loop
    return vis

def update_cnt(cnt):
    return cnt + 1

def mark_and_break(cur, vis, loop):
    loop.add(cur)
    vis = update_vis_loop(vis, loop)
    return True, vis, False    # broke, updated vis, is_cycle

def loop_detect(field, y, x, vis):
    cur = coord_tuple(y, x)
    if already_visited(cur, vis):
        return 0, vis
    loop = initialize_loop(cur)
    cnt = 0
    while True:
        cur = get_next_cur(cur, field)
        if already_visited(cur, vis):
            loop.add(cur)
            vis = update_vis_loop(vis, loop)
            break
        if cur in loop:
            loop.add(cur)
            cnt = update_cnt(cnt)
            vis = update_vis_loop(vis, loop)
            break
        loop.add(cur)
    return cnt, vis

def analyze_field(field, N):
    vis = set()
    cnt = 0
    for y in xrange(N):
        for x in xrange(N):
            c, vis = loop_detect(field, y, x, vis)
            cnt += c
    return cnt

def main_loop():
    while True:
        N = read_N()
        if should_break(N):
            break
        field = build_field(N)
        cnt = analyze_field(field, N)
        print cnt

main_loop()