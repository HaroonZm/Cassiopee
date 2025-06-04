from functools import partial
from itertools import product
import sys
import numpy as np

sys.setrecursionlimit(10**8)
INF = float('inf')
MOD = 10**9 + 7
EPS = 1e-7

def inp():
    return int(sys.stdin.readline())

def inpl():
    return list(map(int, sys.stdin.readline().split()))

def main():
    while True:
        H, W, C = inpl()
        if H == 0:
            break
        board = np.array([inpl() for _ in range(H)], dtype=np.int8)
        ans = 0

        def fill(x, y, s, c, arr):
            stack = [(x, y)]
            while stack:
                cx, cy = stack.pop()
                if 0 <= cx < W and 0 <= cy < H and arr[cy, cx] == s:
                    arr[cy, cx] = c
                    stack.extend(((cx+1,cy),(cx-1,cy),(cx,cy+1),(cx,cy-1)))

        def count_area(x, y, arr):
            stack = [(x, y)]
            cnt = 0
            while stack:
                cx, cy = stack.pop()
                if 0 <= cx < W and 0 <= cy < H and arr[cy, cx] == C:
                    arr[cy, cx] = -1
                    cnt += 1
                    stack.extend(((cx+1,cy),(cx-1,cy),(cx,cy+1),(cx,cy-1)))
            return cnt

        for colors in product(range(1, 7), repeat=4):
            seq = list(colors) + [C]
            cur_board = board.copy()
            for nc in seq:
                if cur_board[0, 0] != nc:
                    fill(0, 0, cur_board[0, 0], nc, cur_board)
            ans = max(ans, count_area(0, 0, cur_board))

        print(ans)

if __name__ == '__main__':
    main()