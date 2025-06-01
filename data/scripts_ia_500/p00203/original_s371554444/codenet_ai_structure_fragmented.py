import sys
from sys import stdin
from collections import deque, defaultdict
input = stdin.readline

def parse_input_line():
    return map(int, input().strip().split())

def read_field(Y):
    field = []
    for _ in range(Y):
        row = read_field_row()
        field.append(row)
    return field

def read_field_row():
    return [int(x) for x in input().strip().split()]

def get_start_positions(field):
    positions = []
    BLANK = 0
    for x, val in enumerate(field[0]):
        if val == BLANK:
            positions.append((x, 0))
    return positions

def pos_key(x, y):
    return '{}_{}'.format(x, y)

def is_inside_field(x, y, x_limit, y_limit):
    return 0 <= x < x_limit and 0 <= y < y_limit

def is_blank(cell):
    return cell == 0

def is_obstacle(cell):
    return cell == 1

def is_jump(cell):
    return cell == 2

def update_path_and_queue(path, Q, key, num):
    if not path[key]:
        Q.append(tuple(map(int, key.split('_'))))
    path[key] += num

def handle_jump_cell(cx, cy, num, field, path, Q, ans):
    y_limit = len(field)
    if cy + 2 > y_limit - 1:
        ans[0] += num
    else:
        k = pos_key(cx, cy + 2)
        update_path_and_queue(path, Q, k, num)

def handle_jump_move(nx, ny, num, field, path, Q, ans):
    y_limit = len(field)
    if ny + 2 > y_limit - 1:
        ans[0] += num
    else:
        k = pos_key(nx, ny + 2)
        update_path_and_queue(path, Q, k, num)

def handle_blank_move(nx, ny, num, field, path, Q, ans):
    y_limit = len(field)
    if ny >= y_limit - 1:
        ans[0] += num
    else:
        k = pos_key(nx, ny)
        update_path_and_queue(path, Q, k, num)

def process_cell(cx, cy, num, field, path, Q, ans, dx, x_limit, y_limit):
    cell = field[cy][cx]
    if is_obstacle(cell):
        return
    elif is_jump(cell):
        handle_jump_cell(cx, cy, num, field, path, Q, ans)
        return
    elif cy == y_limit - 1:
        ans[0] += num
        return

    for i in range(3):
        nx = cx + dx[i]
        ny = cy + 1
        if not is_inside_field(nx, ny, x_limit, y_limit):
            continue
        ncell = field[ny][nx]
        if is_jump(ncell) and dx[i] == 0:
            handle_jump_move(nx, ny, num, field, path, Q, ans)
        elif is_blank(ncell):
            handle_blank_move(nx, ny, num, field, path, Q, ans)

def solve(field):
    BLANK, OBSTACLE, JUMP = 0, 1, 2

    ans = [0]
    dx = [0, -1, 1]
    x_limit = len(field[0])
    y_limit = len(field)

    path = defaultdict(int)
    Q = deque()

    start_positions = get_start_positions(field)
    for x, y in start_positions:
        k = pos_key(x, y)
        Q.append((x, y))
        path[k] = 1

    while Q:
        cx, cy = Q.popleft()
        k = pos_key(cx, cy)
        num = path.pop(k)
        process_cell(cx, cy, num, field, path, Q, ans, dx, x_limit, y_limit)

    return ans[0]

def main(args):
    while True:
        X, Y = parse_input_line()
        if X == 0 and Y == 0:
            break
        field = read_field(Y)
        result = solve(field)
        print(result)

if __name__ == '__main__':
    main(sys.argv[1:])