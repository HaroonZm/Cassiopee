import copy
import itertools
import sys

if sys.version[0] == '2':
    range, input = xrange, raw_input

drc = [(-1, 0), (0, 1), (1, 0), (0, -1)]
C_NUM = 6

while True:
    H, W, C = map(int, input().split())
    if not (H | W | C):
        break
    board = [[int(x) - 1 for x in input().split()] for _ in range(H)]
    ans = 0
    for ope in itertools.product(range(C_NUM), repeat=4):
        # print(ope)
        ps = [(0, 0)]
        tmp_board = copy.deepcopy(board)
        for color in itertools.chain(ope, (C - 1,)):
            now_c = tmp_board[0][0]
            if now_c == color:
                continue

            for r, c in ps:
                tmp_board[r][c] = color
            stack = ps[:]
            while stack:
                r, c = stack.pop()
                for dr, dc in drc:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < H and 0 <= nc < W and tmp_board[nr][nc] == now_c:
                        tmp_board[nr][nc] = color
                        stack.append((nr, nc))
                        ps.append((nr, nc))
        for r, c in ps:
            tmp_board[r][c] = -1
        stack = ps[:]
        while stack:
            r, c = stack.pop()
            for dr, dc in drc:
                nr, nc = r + dr, c + dc
                if 0 <= nr < H and 0 <= nc < W and tmp_board[nr][nc] == C - 1:
                    tmp_board[nr][nc] = -1
                    stack.append((nr, nc))
        cand = sum(row.count(-1) for row in tmp_board)
        if cand > ans:
            ans = cand
    print(ans)