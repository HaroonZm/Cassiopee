from collections import deque
import sys

def read_input():
    return map(int, sys.stdin.readline().split())

def read_board(w, h):
    return [list(map(int, sys.stdin.readline().split())) for _ in range(h)]

def process_cell(cell, id, x, y, s_x, s_y, g_x, g_y):
    if cell == 1:
        return id, 0, s_x, s_y, g_x, g_y
    elif cell == 2:
        return 0, (x, y, g_x, g_y)
    elif cell == 3:
        return 0, (s_x, s_y, x, y)
    else:
        return 0, (s_x, s_y, g_x, g_y)

def update_board(board, w, h):
    id = 1
    s_x = s_y = g_x = g_y = 0
    for y in range(h):
        for x in range(w):
            if board[y][x] == 1:
                board[y][x] = id
                id += 1
            elif board[y][x] == 2:
                s_x, s_y = x, y
                board[y][x] = 0
            elif board[y][x] == 3:
                g_x, g_y = x, y
                board[y][x] = 0
    return s_x, s_y, g_x, g_y, board

def in_bounds(x, y, w, h):
    return 0 <= x < w and 0 <= y < h

def get_neighbors(x, y):
    return [(x-1, y), (x+1, y), (x, y+1), (x, y-1)]

def should_move(board, next_x, next_y, through, count):
    return board[next_y][next_x] in through[:count]

def extend_path(x, y, step, dx, dy, through, count, w, h, board, search_list):
    if step+1 < 11:
        for next_x, next_y in get_neighbors(x, y):
            if in_bounds(next_x, next_y, w, h):
                if should_move(board, next_x, next_y, through, count):
                    search_list.append([next_x, next_y, step+1, next_x-x, next_y-y, through[:count], count])

def slide_along_direction(x, y, dx, dy, g_x, g_y, w, h, board, through, count, step, search_list):
    t_x, t_y = x, y
    drop = False
    goal = False
    while True:
        n_x, n_y = t_x + dx, t_y + dy
        if n_x == g_x and n_y == g_y:
            return step, True
        if in_bounds(n_x, n_y, w, h):
            if board[n_y][n_x] not in through[:count]:
                break
        else:
            drop = True
            break
        t_x += dx
        t_y += dy
    if drop:
        return None, False
    if not goal:
        tmp = board[t_y+dy][t_x+dx]
        new_through = through[:count] + [tmp]
        search_list.append([t_x, t_y, step, 0, 0, new_through, count+1])
    return None, False

def bfs_solver(s_x, s_y, g_x, g_y, w, h, board):
    search_list = deque()
    search_list.append([s_x, s_y, 0, 0, 0, [0], 1])
    ans = -1
    while search_list:
        x, y, step, dx, dy, through, count = search_list.popleft()
        if x == g_x and y == g_y:
            ans = step
            break
        if dx == 0 and dy == 0:
            extend_path(x, y, step, dx, dy, through, count, w, h, board, search_list)
        else:
            out, reached_goal = slide_along_direction(x, y, dx, dy, g_x, g_y, w, h, board, through, count, step+1, search_list)
            if reached_goal:
                ans = out
                break
    return ans

def process_case(w, h):
    board = read_board(w, h)
    s_x, s_y, g_x, g_y, board = update_board(board, w, h)
    ans = bfs_solver(s_x, s_y, g_x, g_y, w, h, board)
    print(ans)

def main():
    while True:
        w, h = read_input()
        if w == 0:
            break
        process_case(w, h)

if __name__ == "__main__":
    main()