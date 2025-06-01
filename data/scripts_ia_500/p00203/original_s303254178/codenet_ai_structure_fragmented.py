import sys
from sys import stdin
from collections import deque, defaultdict
input = stdin.readline

def get_constants():
    return 0, 1, 2

def get_directions():
    dy = [1, 1, 1]
    dx = [0, -1, 1]
    return dy, dx

def get_limits(field):
    x_limit = len(field[0])
    y_limit = len(field)
    return x_limit, y_limit

def make_key(x, y):
    return '{}_{}'.format(x, y)

def initialize_path_and_queue(field, BLANK):
    path = defaultdict(int)
    Q = deque()
    for x, m in enumerate(field[0]):
        if m == BLANK:
            t = make_key(x, 0)
            Q.append((x, 0))
            path[t] = 1
    return path, Q

def process_jump_cell(cx, cy, y_limit, num, Q, path):
    if cy+2 > y_limit-1:
        return num, Q, path, True
    else:
        t = make_key(cx, cy+2)
        if not path[t]:
            Q.append((cx, cy+2))
        path[t] += num
        return 0, Q, path, False

def is_within_horizontal_limits(nx, x_limit):
    return 0 <= nx < x_limit

def handle_jump_condition(nx, ny, dx_i, y_limit, num, Q, path, JUMP):
    if dx_i == 0:
        if ny+2 > y_limit-1:
            return num, Q, path, True
        else:
            t = make_key(nx, ny+2)
            if not path[t]:
                Q.append((nx, ny+2))
            path[t] += num
            return 0, Q, path, False
    return 0, Q, path, False

def handle_blank_condition(nx, ny, y_limit, num, Q, path):
    if ny >= y_limit -1:
        return num, Q, path, True
    else:
        t = make_key(nx, ny)
        if not path[t]:
            Q.append((nx, ny))
        path[t] += num
        return 0, Q, path, False

def process_adjacent_cells(cx, cy, dy, dx, x_limit, y_limit, field, num, Q, path, BLANK, JUMP):
    ans_increment = 0
    for i in range(len(dy)):
        nx = cx + dx[i]
        ny = cy + dy[i]
        if not is_within_horizontal_limits(nx, x_limit):
            continue
        if field[ny][nx] == JUMP:
            inc, Q, path, finished = handle_jump_condition(nx, ny, dx[i], y_limit, num, Q, path, JUMP)
            if finished:
                ans_increment += inc
        elif field[ny][nx] == BLANK:
            inc, Q, path, finished = handle_blank_condition(nx, ny, y_limit, num, Q, path)
            if finished:
                ans_increment += inc
    return ans_increment, Q, path

def handle_current_cell(cx, cy, y_limit, field, path, Q, num, BLANK, OBSTACLE, JUMP):
    ans_increment = 0
    if field[cy][cx] == OBSTACLE:
        return ans_increment, Q, path, False
    elif field[cy][cx] == JUMP:
        inc, Q, path, finished = process_jump_cell(cx, cy, y_limit, num, Q, path)
        if finished:
            ans_increment += inc
        return ans_increment, Q, path, True
    elif cy == y_limit -1:
        ans_increment += num
        return ans_increment, Q, path, True
    return ans_increment, Q, path, False

def solve(field):
    BLANK, OBSTACLE, JUMP = get_constants()
    dy, dx = get_directions()
    x_limit, y_limit = get_limits(field)
    path, Q = initialize_path_and_queue(field, BLANK)
    ans = 0
    while Q:
        cx, cy = Q.popleft()
        t = make_key(cx, cy)
        num = path.pop(t)
        inc, Q, path, finished = handle_current_cell(cx, cy, y_limit, field, path, Q, num, BLANK, OBSTACLE, JUMP)
        ans += inc
        if finished:
            continue
        inc_adj, Q, path = process_adjacent_cells(cx, cy, dy, dx, x_limit, y_limit, field, num, Q, path, BLANK, JUMP)
        ans += inc_adj
    return ans

def read_dimensions():
    return map(int, input().strip().split())

def read_field(Y):
    field = []
    for _ in range(Y):
        line = [int(x) for x in input().strip().split()]
        field.append(line)
    return field

def main(args):
    while True:
        X, Y = read_dimensions()
        if X == 0 and Y == 0:
            break
        field = read_field(Y)
        result = solve(field)
        print(result)

if __name__ == '__main__':
    main(sys.argv[1:])