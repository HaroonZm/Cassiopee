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
        row = [int(x)-1 for x in input().split()]
        board.append(row)
    ans = 0
    for ope in itertools.product(range(C_NUM), repeat=4):
        if ope[0] == board[0][0] or ope[-1] == C-1:
            continue
        b = False
        for i in range(3):
            if ope[i] == ope[i+1]:
                b = True
                break
        if b:
            continue
        tmp_board = copy.deepcopy(board)
        for color in ope:
            st = [(0,0)]
            now_c = tmp_board[0][0]
            next_c = color
            if now_c == next_c:
                continue
            vis = [[False]*W for _ in range(H)]
            while st:
                r,c = st.pop()
                if not (0<=r<H and 0<=c<W):
                    continue
                if tmp_board[r][c] != now_c:
                    continue
                if vis[r][c]:
                    continue
                tmp_board[r][c] = next_c
                vis[r][c] = True
                for dr,dc in drc:
                    nr = r+dr
                    nc = c+dc
                    st.append((nr,nc))
        now_c = tmp_board[0][0]
        next_c = C-1
        st = [(0,0)]
        vis = [[False]*W for _ in range(H)]
        while st:
            r,c = st.pop()
            if not (0<=r<H and 0<=c<W):
                continue
            if tmp_board[r][c] != now_c:
                continue
            if vis[r][c]:
                continue
            tmp_board[r][c] = next_c
            vis[r][c] = True
            for dr,dc in drc:
                nr = r+dr
                nc = c+dc
                st.append((nr,nc))
        now_c = tmp_board[0][0]
        next_c = -1
        st = [(0,0)]
        vis = [[False]*W for _ in range(H)]
        while st:
            r,c = st.pop()
            if not (0<=r<H and 0<=c<W):
                continue
            if tmp_board[r][c] != now_c:
                continue
            if vis[r][c]:
                continue
            tmp_board[r][c] = next_c
            vis[r][c] = True
            for dr,dc in drc:
                nr = r+dr
                nc = c+dc
                st.append((nr,nc))
        cand = 0
        for row in tmp_board:
            for v in row:
                if v == -1:
                    cand += 1
        if cand > ans:
            ans = cand
    print(ans)