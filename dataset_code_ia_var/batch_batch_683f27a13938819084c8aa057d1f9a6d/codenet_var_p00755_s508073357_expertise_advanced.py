import sys
import itertools
from copy import deepcopy

if sys.version_info[0] == 2:
    range, input = xrange, raw_input

drc = [(-1, 0), (0, 1), (1, 0), (0, -1)]
C_NUM = 6

def dfs(r, c, now_c, next_c, board, H, W):
    stack = [(r, c)]
    while stack:
        i, j = stack.pop()
        board[i][j] = next_c
        stack.extend(
            (ni, nj)
            for di, dj in drc
            if 0 <= (ni := i + di) < H and 0 <= (nj := j + dj) < W and board[ni][nj] == now_c
        )

def solve(H, W, C, board):
    ans = 0
    rng = range(C_NUM)
    candidates = (
        ope for ope in itertools.product(rng, repeat=5)
        if ope[0] != board[0][0]
           and ope[-1] == C - 1
           and all(ope[i] != ope[i + 1] for i in range(4))
    )
    for ope in candidates:
        tmp_board = deepcopy(board)
        cur_color = tmp_board[0][0]
        for color in ope:
            if cur_color != color:
                dfs(0, 0, cur_color, color, tmp_board, H, W)
                cur_color = color
        dfs(0, 0, cur_color, -1, tmp_board, H, W)
        ans = max(ans, sum(row.count(-1) for row in tmp_board))
    return ans

def main():
    while True:
        HWC = input()
        if not HWC:
            continue
        H, W, C = map(int, HWC.split())
        if not (H | W | C):
            break
        board = [list(map(lambda x: int(x)-1, input().split())) for _ in range(H)]
        print(solve(H, W, C, board))

if __name__ == "__main__":
    main()