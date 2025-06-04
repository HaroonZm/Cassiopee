import sys
sys.setrecursionlimit(10**7)

H, W = map(int, input().split())
board = [list(input()) for _ in range(H)]

# Directions: up, down, left, right
directions = [(-1,0),(1,0),(0,-1),(0,1)]

from copy import deepcopy

from functools import lru_cache

def to_tuple(board):
    return tuple(tuple(row) for row in board)

@lru_cache(maxsize=None)
def dfs(state):
    board = [list(row) for row in state]
    for r in range(H):
        for c in range(W):
            if board[r][c] == '.':
                new_board = deepcopy(board)
                # Place walls from chosen cell in four directions
                for dr, dc in directions:
                    nr, nc = r, c
                    while 0 <= nr < H and 0 <= nc < W:
                        if new_board[nr][nc] == '#':
                            break
                        new_board[nr][nc] = '#'
                        nr += dr
                        nc += dc
                # After move, opponent moves
                if not dfs(to_tuple(new_board)):
                    return True
    return False

initial_state = to_tuple(tuple(row) for row in board)
print("First" if dfs(initial_state) else "Second")