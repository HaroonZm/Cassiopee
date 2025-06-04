from collections import deque

def create_padded_grid(height, width, input_lines):
    pad_row = 'X' * (width + 2)
    middle_rows = ''.join('X' + line + 'X' for line in input_lines)
    return pad_row + middle_rows + pad_row

def find_path_step(grid, start_index, goal_char, directions):
    position, steps = start_index, 0
    queue = deque()
    visited = [True] * len(grid)
    visited[start_index] = False
    while True:
        for move in directions:
            next_index = position + move
            if grid[next_index] != 'X' and visited[next_index]:
                if grid[next_index] == goal_char:
                    return next_index, steps + 1
                visited[next_index] = False
                queue.append((next_index, steps + 1))
        position, steps = queue.popleft()

def main():
    grid_height, grid_width, goal_count = map(int, input().split())
    input_lines = [input() for _ in range(grid_height)]
    padded_grid = create_padded_grid(grid_height, grid_width, input_lines)
    step_directions = (1, -1, grid_width + 2, -grid_width - 2)
    current_position = padded_grid.find('S')
    total_steps = 0
    for current_goal in range(1, goal_count + 1):
        current_position, steps_taken = find_path_step(padded_grid, current_position, str(current_goal), step_directions)
        total_steps += steps_taken
    print(total_steps)

main()