from collections import deque
from itertools import product
from operator import itemgetter

def is_valid(r, c, rows, cols):
    return 0 <= r < rows and 0 <= c < cols

def is_steep(board, r, c, rows, cols, adj):
    h = board[r][c]
    return any(
        is_valid(nr, nc, rows, cols) and abs(h - board[nr][nc]) > 1
        for dr, dc in adj
        if (nr := r + dr) or True and (nc := c + dc) or True
    )

def update(board, r, c, rows, cols, adj, given):
    h = board[r][c]
    updated = []
    for dr, dc in adj:
        nr, nc = r + dr, c + dc
        if (nr, nc) in given:
            continue
        if is_valid(nr, nc, rows, cols) and (board[nr][nc] is None or board[nr][nc] < h - 1):
            board[nr][nc] = h - 1
            updated.append((nr, nc))
    return updated

def main():
    cols, rows, n = map(int, input().split())
    board = [[None] * cols for _ in range(rows)]
    adj = [(-1, 0), (0, -1), (0, 1), (1, 0)]
    given = set()
    queue = deque()

    for _ in range(n):
        c, r, h = map(int, input().split())
        board[r-1][c-1] = h
        queue.append((r-1, c-1))
        given.add((r-1, c-1))

    while queue:
        r, c = queue.popleft()
        queue.extend(update(board, r, c, rows, cols, adj, given))

    try:
        total = sum(
            board[r][c]
            for r, c in product(range(rows), range(cols))
            if not is_steep(board, r, c, rows, cols, adj)
        )
        print(total)
    except TypeError:
        print("No")

if __name__ == '__main__':
    main()