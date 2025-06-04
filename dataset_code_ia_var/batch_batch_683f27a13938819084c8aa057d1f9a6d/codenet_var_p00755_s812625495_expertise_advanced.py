import sys
import numpy as np
from itertools import product

if sys.version_info[0] == 2:
    range, input = xrange, raw_input

DIRECTIONS = np.array([[-1, 0], [0, 1], [1, 0], [0, -1]])
C_NUM = 6

def dfs_fast(board, r, c, now_c, next_c):
    H, W = board.shape
    stack = [(r, c)]
    while stack:
        x, y = stack.pop()
        if board[x, y] != now_c:
            continue
        board[x, y] = next_c
        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            if 0 <= nx < H and 0 <= ny < W and board[nx, ny] == now_c:
                stack.append((nx, ny))

def parse_input():
    while True:
        values = input().split()
        H, W, C = map(int, values)
        if not (H | W | C):
            break
        grid = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(H)]
        yield H, W, C, np.array(grid, dtype=np.int8)

for H, W, C, board in parse_input():
    best = 0
    for ops in product(range(C_NUM), repeat=4):
        if ops[0] == board[0, 0] or ops[-1] == C - 1 or any(ops[i] == ops[i + 1] for i in range(3)):
            continue
        tmp = board.copy()
        for color in ops:
            dfs_fast(tmp, 0, 0, tmp[0, 0], color)
        dfs_fast(tmp, 0, 0, tmp[0, 0], C - 1)
        dfs_fast(tmp, 0, 0, tmp[0, 0], -1)
        count = np.sum(tmp == -1)
        if count > best:
            best = count
    print(best)