import sys
from collections import deque

def can_throw(board, x, y, dx, dy, w, h):
    nx, ny = x + dx, y + dy
    if 0 <= nx < h and 0 <= ny < w:
        if board[nx][ny] == 1:
            return False
        else:
            return True
    return False

def solve(w, h, board):
    start = None
    goal = None
    for i in range(h):
        for j in range(w):
            if board[i][j] == 2:
                start = (i, j)
            elif board[i][j] == 3:
                goal = (i, j)

    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    max_moves = 10

    queue = deque()
    queue.append( (start[0], start[1], 0, board) )
    visited = set()

    def board_to_tuple(b):
        return tuple(tuple(row) for row in b)

    visited.add( (start[0], start[1], board_to_tuple(board)) )

    while queue:
        x, y, moves, b = queue.popleft()

        if moves >= max_moves:
            continue
        for dx, dy in directions:
            if not can_throw(b, x, y, dx, dy, w, h):
                continue
            # move stone in direction dx, dy until hit a block or goal or out of board
            nx, ny = x, y
            while True:
                nx += dx
                ny += dy
                if not (0 <= nx < h and 0 <= ny < w):
                    # stone goes out of board, failure, discard this move
                    nx = -1
                    break
                if b[nx][ny] == 1:
                    # hits a block, stops at previous square
                    nx -= dx
                    ny -= dy
                    break
                if b[nx][ny] == 3:
                    # reached goal
                    return moves+1
            if nx == -1 and ny == -1:
                # out of board, skip
                continue
            if (nx, ny) == (x, y):
                # no movement, skip
                continue

            # Remove the block that was hit if any
            new_board = [list(row) for row in b]
            # block position is position next to where stone stopped in movement direction
            block_x, block_y = nx + dx, ny + dy
            if 0 <= block_x < h and 0 <= block_y < w:
                if new_board[block_x][block_y] == 1:
                    new_board[block_x][block_y] = 0

            state_tuple = (nx, ny, board_to_tuple(new_board))
            if state_tuple in visited:
                continue
            visited.add(state_tuple)
            queue.append( (nx, ny, moves+1, new_board) )

    return -1

def main():
    input_lines = sys.stdin.read().strip().split('\n')
    idx = 0
    while True:
        if idx >= len(input_lines):
            break
        line = input_lines[idx]
        idx += 1
        if line == '0 0':
            break
        w, h = map(int, line.split())
        board = []
        for _ in range(h):
            row = list(map(int, input_lines[idx].split()))
            idx +=1
            board.append(row)
        print(solve(w, h, board))

if __name__ == '__main__':
    main()