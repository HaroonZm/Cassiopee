import sys
_input_readline = sys.stdin.readline

import collections
_Coord = collections.namedtuple('Coord', ['x', 'y'])
_StructBlock = collections.namedtuple('StructBlock', ['color', 'direction', 'x', 'y'])

def get_block_coverage(block):
    base_x, base_y = block.x, block.y
    square_offset = [(0, 0), (1, 0), (0, 1), (1, 1)]
    for offset_x, offset_y in square_offset:
        yield base_x + offset_x, base_y + offset_y
    if block.direction:
        extended_y = base_y + 2
        extended_x = base_x
    else:
        extended_x = base_x + 2
        extended_y = base_y
    for offset_x, offset_y in square_offset:
        yield extended_x + offset_x, extended_y + offset_y

def fill_color(board_grid, coord_start, fill_value):
    source_color = board_grid[coord_start.y][coord_start.x]
    if source_color == 0:
        return
    queue_coords = [(coord_start.x, coord_start.y)]
    while queue_coords:
        current_x, current_y = queue_coords.pop()
        if board_grid[current_y][current_x] == source_color:
            board_grid[current_y][current_x] = fill_value
            neighbor_shifts = [(-1, 0), (0, -1), (1, 0), (0, 1)]
            for dx, dy in neighbor_shifts:
                neighbor_x, neighbor_y = current_x + dx, current_y + dy
                if 0 <= neighbor_x < len(board_grid[0]) and 0 <= neighbor_y < len(board_grid):
                    queue_coords.append((neighbor_x, neighbor_y))

def check_path_exists(field_size, coord_start, coord_goal, block_list):
    board_matrix = [[0 for _ in range(field_size.x + 2)] for _ in range(field_size.y + 2)]
    for block_obj in block_list:
        for covered_x, covered_y in get_block_coverage(block_obj):
            board_matrix[covered_y][covered_x] = block_obj.color
    fill_color(board_matrix, coord_start, -1)
    return board_matrix[coord_goal.y][coord_goal.x] == -1

while True:
    size_input = _input_readline().split()
    field_size = _Coord(*map(int, size_input))
    if field_size.x == 0:
        break
    coord_start = _Coord(*map(int, _input_readline().split()))
    coord_goal = _Coord(*map(int, _input_readline().split()))
    block_obj_list = []
    block_count = int(_input_readline())
    for _ in range(block_count):
        block_tuple = list(map(int, _input_readline().split()))
        block_obj_list.append(_StructBlock(*block_tuple))
    result = check_path_exists(field_size, coord_start, coord_goal, block_obj_list)
    print('OK' if result else 'NG')