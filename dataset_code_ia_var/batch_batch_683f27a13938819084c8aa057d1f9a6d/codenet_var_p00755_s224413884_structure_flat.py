import copy
import itertools
import sys

if sys.version[0] == '2':
    range, input = xrange, raw_input

drc = [(-1, 0), (0, 1), (1, 0), (0, -1)]
C_NUM = 6

while True:
    tmp = input()
    if not tmp.strip():
        continue
    HWC = tmp.split()
    if len(HWC) < 3:
        HWC += input().split()
    H, W, C = map(int, HWC)
    if H == 0 and W == 0 and C == 0:
        break
    board = []
    for _ in range(H):
        row = []
        for value in input().split():
            row.append(int(value) - 1)
        board.append(row)
    ans = 0
    for ope in itertools.product(range(C_NUM), repeat=4):
        ps = [(0, 0)]
        tmp_board = copy.deepcopy(board)
        for color in list(ope) + [C - 1]:
            now_c = tmp_board[0][0]
            if now_c == color:
                continue
            for t in ps:
                tmp_board[t[0]][t[1]] = color
            stack = []
            for t in ps:
                stack.append((t[0], t[1]))
            nps = ps[:]
            while stack:
                rc = stack.pop()
                for d in drc:
                    nr = rc[0] + d[0]
                    nc = rc[1] + d[1]
                    if 0 <= nr < H and 0 <= nc < W and tmp_board[nr][nc] == now_c:
                        tmp_board[nr][nc] = color
                        stack.append((nr, nc))
                        if (nr, nc) not in nps:
                            nps.append((nr, nc))
            ps = nps
        for t in ps:
            tmp_board[t[0]][t[1]] = -1
        stack = []
        for t in ps:
            stack.append((t[0], t[1]))
        while stack:
            rc = stack.pop()
            for d in drc:
                nr = rc[0] + d[0]
                nc = rc[1] + d[1]
                if 0 <= nr < H and 0 <= nc < W and tmp_board[nr][nc] == C - 1:
                    tmp_board[nr][nc] = -1
                    stack.append((nr, nc))
        cand = 0
        for row in tmp_board:
            for v in row:
                if v == -1:
                    cand += 1
        if cand > ans:
            ans = cand
    print(ans)