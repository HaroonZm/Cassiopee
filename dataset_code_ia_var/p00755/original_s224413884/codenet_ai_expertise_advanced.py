import sys
import itertools
from collections import deque

C_NUM = 6
drc = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def readints():
    return map(int, sys.stdin.readline().split())

range_fn = range  # Python 3 compatibility by default

while True:
    H, W, C = readints()
    if not (H | W | C):
        break
    board = [list(map(lambda x: int(x) - 1, sys.stdin.readline().split())) for _ in range(H)]
    ans = 0
    for ops in itertools.product(range_fn(C_NUM), repeat=4):
        tmp_board = [row[:] for row in board]
        marked = set([(0, 0)])
        for color in (*ops, C - 1):
            start_color = tmp_board[0][0]
            if start_color == color:
                continue
            queue = deque(marked)
            while queue:
                r, c = queue.popleft()
                tmp_board[r][c] = color
                for dr, dc in drc:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < H and 0 <= nc < W and (nr, nc) not in marked and tmp_board[nr][nc] == start_color:
                        marked.add((nr, nc))
                        queue.append((nr, nc))
        # Flood fill with -1 for the target color region
        queue = deque(marked)
        seen = set(marked)
        for r, c in marked:
            tmp_board[r][c] = -1
        while queue:
            r, c = queue.popleft()
            for dr, dc in drc:
                nr, nc = r + dr, c + dc
                if 0 <= nr < H and 0 <= nc < W and (nr, nc) not in seen and tmp_board[nr][nc] == C - 1:
                    tmp_board[nr][nc] = -1
                    seen.add((nr, nc))
                    queue.append((nr, nc))
        ans = max(ans, sum(cell == -1 for row in tmp_board for cell in row))
    print(ans)