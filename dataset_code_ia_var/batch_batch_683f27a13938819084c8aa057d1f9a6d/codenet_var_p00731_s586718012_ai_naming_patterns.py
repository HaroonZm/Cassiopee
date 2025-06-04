import sys
import heapq

def read_input():
    return sys.stdin.readline()

def initialize_board(height, width):
    return [read_input().strip().split() for _ in range(height)]

def initialize_visited(height, width):
    return [[[False, False] for _ in range(width)] for _ in range(height)]

def find_start_positions(board, height, width):
    start_positions = []
    for row_idx in range(height):
        for col_idx in range(width):
            if board[row_idx][col_idx] == "S":
                start_positions.append((col_idx, row_idx))
    return start_positions

def get_next_positions_right_foot(x, y):
    return [(x+1, y-2), (x+1, y-1), (x+1, y), (x+1, y+1), (x+1, y+2), (x+2, y-1), (x+2, y), (x+2, y+1), (x+3, y)]

def get_next_positions_left_foot(x, y):
    return [(x-3, y), (x-2, y-1), (x-2, y), (x-2, y+1), (x-1, y-2), (x-1, y-1), (x-1, y), (x-1, y+1), (x-1, y+2)]

def process_board(width, height, board):
    visited = initialize_visited(height, width)
    priority_queue = []
    start_positions = find_start_positions(board, height, width)
    for start_x, start_y in start_positions:
        for foot_state in range(2):
            visited[start_y][start_x][foot_state] = True
            heapq.heappush(priority_queue, (0, foot_state, start_x, start_y))
    found_target = False
    while priority_queue:
        current_cost, current_foot, current_x, current_y = heapq.heappop(priority_queue)
        if current_foot == 0:
            next_moves = get_next_positions_right_foot(current_x, current_y)
        else:
            next_moves = get_next_positions_left_foot(current_x, current_y)
        next_foot = (current_foot + 1) % 2
        for next_x, next_y in next_moves:
            if 0 <= next_x < width and 0 <= next_y < height:
                cell_value = board[next_y][next_x]
                if cell_value == "T":
                    print(current_cost)
                    found_target = True
                    break
                if not visited[next_y][next_x][next_foot] and cell_value != "X":
                    visited[next_y][next_x][next_foot] = True
                    heapq.heappush(priority_queue, (current_cost + int(cell_value), next_foot, next_x, next_y))
        if found_target:
            break
    if not found_target:
        print(-1)

def main_loop():
    while True:
        width, height = map(int, read_input().split())
        if width == 0:
            break
        board = initialize_board(height, width)
        process_board(width, height, board)

if __name__ == "__main__":
    main_loop()