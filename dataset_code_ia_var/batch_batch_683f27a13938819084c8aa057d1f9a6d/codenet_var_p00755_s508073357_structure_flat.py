import copy
import itertools
import sys

if sys.version[0] == '2':
    range, input = xrange, raw_input

drc = [(-1, 0), (0, 1), (1, 0), (0, -1)]
C_NUM = 6

while True:
    HWC = input().split()
    H, W, C = map(int, HWC)
    if not (H or W or C):
        break
    board = []
    for _ in range(H):
        board.append([int(x) - 1 for x in input().split()])
    ans = 0
    for ope in itertools.product(range(C_NUM), repeat=5):
        if ope[0] == board[0][0] or ope[-1] != C - 1 or ope[0] == ope[1] or ope[1] == ope[2] or ope[2] == ope[3] or ope[3] == ope[4]:
            continue
        tmp_board = copy.deepcopy(board)
        color_idx = 0
        while color_idx < 5:
            stack = [(0,0)]
            old_color = tmp_board[0][0]
            new_color = ope[color_idx]
            if old_color == new_color:
                color_idx += 1
                continue
            while stack:
                r, c = stack.pop()
                if tmp_board[r][c] != old_color:
                    continue
                tmp_board[r][c] = new_color
                for dr, dc in drc:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < H and 0 <= nc < W:
                        if tmp_board[nr][nc] == old_color:
                            stack.append((nr, nc))
            color_idx += 1
        # Last fill to mark region with -1
        stack = [(0,0)]
        old_color = tmp_board[0][0]
        if old_color == -1:
            cand = sum(row.count(-1) for row in tmp_board)
            if cand > ans:
                ans = cand
            continue
        new_color = -1
        while stack:
            r, c = stack.pop()
            if tmp_board[r][c] != old_color:
                continue
            tmp_board[r][c] = new_color
            for dr, dc in drc:
                nr, nc = r + dr, c + dc
                if 0 <= nr < H and 0 <= nc < W:
                    if tmp_board[nr][nc] == old_color:
                        stack.append((nr, nc))
        cand = sum(row.count(-1) for row in tmp_board)
        if cand > ans:
            ans = cand
    print(ans)