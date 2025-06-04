import sys
from collections import deque

input_reader = sys.stdin.readline
output_writer = sys.stdout.write

def get_next_input():
    width, height = map(int, input_reader().split())
    if width == height == 0:
        return None, None, None
    grid_lines = [input_reader().strip() for _ in range(height)]
    return width, height, grid_lines

def get_position(grid, symbol):
    for row_index, row in enumerate(grid):
        for col_index, cell in enumerate(row):
            if cell == symbol:
                return row_index, col_index
    return None, None

def find_direction(grid, row, col, directions):
    final_dir = 0
    for dir_idx, (dx, dy) in enumerate(directions):
        if grid[row + dy][col + dx] != "#":
            final_dir = dir_idx
    return final_dir

def simulate_slide(grid, start_row, start_col, direction, directions):
    dx, dy = directions[direction]
    current_row, current_col = start_row, start_col
    while grid[current_row + dy][current_col + dx] != "#":
        current_row += dy
        current_col += dx
    return current_row, current_col

def build_graph(width, height, grid, directions):
    node_count = width * height * 4
    transitions_0 = [[[] for _ in range(2)] for _ in range(node_count)]
    transitions_1 = [[[] for _ in range(2)] for _ in range(node_count)]
    for row in range(height):
        for col in range(width):
            if grid[row][col] == "#":
                continue
            for dir_idx in range(4):
                dx, dy = directions[dir_idx]
                curr_row, curr_col = row, col
                while grid[curr_row + dy][curr_col + dx] != "#":
                    curr_row += dy
                    curr_col += dx
                prev_dx, prev_dy = directions[(dir_idx - 1) % 4]
                if grid[row + prev_dy][col + prev_dx] == "#":
                    from_node = (row * width + col) * 4 + ((dir_idx - 1) % 4)
                    to_node = (curr_row * width + curr_col) * 4 + dir_idx
                    transitions_0[from_node][1].append(to_node)
                    transitions_1[to_node][1].append(from_node)
                next_dx, next_dy = directions[(dir_idx + 1) % 4]
                if grid[row + next_dy][col + next_dx] == "#":
                    from_node = (row * width + col) * 4 + ((dir_idx + 1) % 4)
                    to_node = (curr_row * width + curr_col) * 4 + dir_idx
                    transitions_0[from_node][0].append(to_node)
                    transitions_1[to_node][0].append(from_node)
    return transitions_0, transitions_1, node_count

def process_grid(width, height, grid):
    direction_moves = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    kitchen_row, kitchen_col = get_position(grid, "K")
    master_row, master_col = get_position(grid, "M")

    kitchen_dir = find_direction(grid, kitchen_row, kitchen_col, direction_moves)
    master_dir = find_direction(grid, master_row, master_col, direction_moves)

    kitchen_slide_row, kitchen_slide_col = simulate_slide(grid, kitchen_row, kitchen_col, kitchen_dir, direction_moves)
    master_slide_row, master_slide_col = simulate_slide(grid, master_row, master_col, master_dir, direction_moves)

    graph0, graph1, total_nodes = build_graph(width, height, grid, direction_moves)

    node_pairs_explored = set()
    queue = deque()
    for starting_dir in range(4):
        if starting_dir != kitchen_dir:
            start_state = ((kitchen_slide_row * width + kitchen_slide_col) * 4 + kitchen_dir,
                           (kitchen_row * width + kitchen_col) * 4 + starting_dir)
            queue.append(start_state)
            node_pairs_explored.add(start_state)

    while queue:
        node_from, node_to = queue.popleft()
        for transition_type in range(2):
            for next_from in graph0[node_from][transition_type]:
                for next_to in graph1[node_to][transition_type ^ 1]:
                    state_pair = (next_from, next_to)
                    if state_pair not in node_pairs_explored:
                        queue.append(state_pair)
                        node_pairs_explored.add(state_pair)

    found_path = False
    for direction_idx in range(4):
        if direction_idx != master_dir:
            possible_state = ((master_row * width + master_col) * 4 + direction_idx,
                              (master_slide_row * width + master_slide_col) * 4 + master_dir)
            if possible_state in node_pairs_explored:
                found_path = True
    if found_path:
        output_writer("He can accomplish his mission.\n")
        return True

    slide_start_node = (kitchen_slide_row * width + kitchen_slide_col) * 4 + kitchen_dir
    single_visited = [False] * total_nodes
    single_visited[slide_start_node] = True
    node_queue = deque([slide_start_node])
    while node_queue:
        current_node = node_queue.popleft()
        for transition_0_node in graph0[current_node][0]:
            if not single_visited[transition_0_node]:
                single_visited[transition_0_node] = True
                node_queue.append(transition_0_node)
        for transition_1_node in graph0[current_node][1]:
            if not single_visited[transition_1_node]:
                single_visited[transition_1_node] = True
                node_queue.append(transition_1_node)
    found_return_path = False
    for direction_idx in range(4):
        if single_visited[(master_row * width + master_col) * 4 + direction_idx]:
            found_return_path = True
    if found_return_path:
        output_writer("He cannot return to the kitchen.\n")
    else:
        output_writer("He cannot bring tea to his master.\n")
    return True

if __name__ == "__main__":
    while True:
        w, h, s_map = get_next_input()
        if w is None:
            break
        process_grid(w, h, s_map)