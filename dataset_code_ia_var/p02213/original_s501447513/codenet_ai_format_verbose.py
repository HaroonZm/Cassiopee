#!/usr/bin/env python3

import sys

from collections import deque

sys.setrecursionlimit(10**6)

read_line_from_input = sys.stdin.readline

grid_height, grid_width = map(int, read_line_from_input().split())

adjacency_list = [[] for _ in range(8 * grid_width * grid_height)]

grid = []

for current_row_index in range(grid_height):
    input_line = read_line_from_input().rstrip()
    grid.append(input_line)

last_cell_is_wall = (grid[grid_height - 1][grid_width - 1] == "#")

if last_cell_is_wall:
    print("NO")
    exit()

def compute_node_index(cell_row, cell_column, direction_state):
    return cell_row * grid_width * 8 + cell_column * 8 + direction_state 

def extract_cell_info_from_index(node_index):
    cell_row = node_index // (grid_width * 8)
    node_index %= (grid_width * 8)
    cell_column = node_index // 8
    node_index %= 8
    direction_state = node_index
    return cell_row, cell_column, direction_state

grid_size_is_even = (grid_height % 2 == 0 and grid_width % 2 == 0)

if grid_size_is_even:
    print("NO")
    exit()

for cell_row in range(grid_height):
    for cell_column in range(grid_width):
        current_cell_value = grid[cell_row][cell_column]
        if current_cell_value in "#16":
            continue
        # Handle Up-Down connections
        if cell_row % 2 == 1 and cell_column % 2 == 0 and cell_row + 1 < grid_height:
            top_cell_value = grid[cell_row - 1][cell_column]
            bottom_cell_value = grid[cell_row + 1][cell_column]
            if (top_cell_value not in "#2345" 
                and bottom_cell_value not in "#2345"
                and int(top_cell_value) + int(bottom_cell_value) == 7):
                corridor_type = int(current_cell_value)
                if corridor_type == 2:
                    # 0 -> 4, 6 -> 2
                    adjacency_list[compute_node_index(cell_row - 1, cell_column, 0)].append(compute_node_index(cell_row + 1, cell_column, 4))
                    adjacency_list[compute_node_index(cell_row - 1, cell_column, 6)].append(compute_node_index(cell_row + 1, cell_column, 2))
                    adjacency_list[compute_node_index(cell_row + 1, cell_column, 4)].append(compute_node_index(cell_row - 1, cell_column, 0))
                    adjacency_list[compute_node_index(cell_row + 1, cell_column, 2)].append(compute_node_index(cell_row - 1, cell_column, 6))
                if corridor_type == 3:
                    # 1 -> 7, 5 -> 3
                    adjacency_list[compute_node_index(cell_row - 1, cell_column, 1)].append(compute_node_index(cell_row + 1, cell_column, 7))
                    adjacency_list[compute_node_index(cell_row - 1, cell_column, 5)].append(compute_node_index(cell_row + 1, cell_column, 3))
                    adjacency_list[compute_node_index(cell_row + 1, cell_column, 7)].append(compute_node_index(cell_row - 1, cell_column, 1))
                    adjacency_list[compute_node_index(cell_row + 1, cell_column, 3)].append(compute_node_index(cell_row - 1, cell_column, 5))
                if corridor_type == 4:
                    # 3 -> 5, 7 -> 1
                    adjacency_list[compute_node_index(cell_row - 1, cell_column, 3)].append(compute_node_index(cell_row + 1, cell_column, 5))
                    adjacency_list[compute_node_index(cell_row - 1, cell_column, 7)].append(compute_node_index(cell_row + 1, cell_column, 1))
                    adjacency_list[compute_node_index(cell_row + 1, cell_column, 5)].append(compute_node_index(cell_row - 1, cell_column, 3))
                    adjacency_list[compute_node_index(cell_row + 1, cell_column, 1)].append(compute_node_index(cell_row - 1, cell_column, 7))
                if corridor_type == 5:
                    # 2 -> 6, 4 -> 0
                    adjacency_list[compute_node_index(cell_row - 1, cell_column, 2)].append(compute_node_index(cell_row + 1, cell_column, 6))
                    adjacency_list[compute_node_index(cell_row - 1, cell_column, 4)].append(compute_node_index(cell_row + 1, cell_column, 0))
                    adjacency_list[compute_node_index(cell_row + 1, cell_column, 6)].append(compute_node_index(cell_row - 1, cell_column, 2))
                    adjacency_list[compute_node_index(cell_row + 1, cell_column, 0)].append(compute_node_index(cell_row - 1, cell_column, 4))
        # Handle Right-Left connections
        if cell_row % 2 == 0 and cell_column % 2 == 1 and cell_column + 1 < grid_width:
            left_cell_value = grid[cell_row][cell_column - 1]
            right_cell_value = grid[cell_row][cell_column + 1]
            if (left_cell_value not in "#2345"
                and right_cell_value not in "#2345"
                and int(left_cell_value) + int(right_cell_value) == 7):
                corridor_type = int(current_cell_value)
                if corridor_type == 2:
                    # 3 -> 7, 5 -> 1
                    adjacency_list[compute_node_index(cell_row, cell_column - 1, 3)].append(compute_node_index(cell_row, cell_column + 1, 7))
                    adjacency_list[compute_node_index(cell_row, cell_column - 1, 5)].append(compute_node_index(cell_row, cell_column + 1, 1))
                    adjacency_list[compute_node_index(cell_row, cell_column + 1, 7)].append(compute_node_index(cell_row, cell_column - 1, 3))
                    adjacency_list[compute_node_index(cell_row, cell_column + 1, 1)].append(compute_node_index(cell_row, cell_column - 1, 5))
                if corridor_type == 5:
                    # 7 -> 3, 1 -> 5
                    adjacency_list[compute_node_index(cell_row, cell_column - 1, 7)].append(compute_node_index(cell_row, cell_column + 1, 3))
                    adjacency_list[compute_node_index(cell_row, cell_column - 1, 1)].append(compute_node_index(cell_row, cell_column + 1, 5))
                    adjacency_list[compute_node_index(cell_row, cell_column + 1, 3)].append(compute_node_index(cell_row, cell_column - 1, 7))
                    adjacency_list[compute_node_index(cell_row, cell_column + 1, 5)].append(compute_node_index(cell_row, cell_column - 1, 1))
                if corridor_type == 3:
                    # 0 -> 6, 4 -> 2
                    adjacency_list[compute_node_index(cell_row, cell_column - 1, 0)].append(compute_node_index(cell_row, cell_column + 1, 6))
                    adjacency_list[compute_node_index(cell_row, cell_column - 1, 4)].append(compute_node_index(cell_row, cell_column + 1, 2))
                    adjacency_list[compute_node_index(cell_row, cell_column + 1, 6)].append(compute_node_index(cell_row, cell_column - 1, 0))
                    adjacency_list[compute_node_index(cell_row, cell_column + 1, 2)].append(compute_node_index(cell_row, cell_column - 1, 4))
                if corridor_type == 4:
                    # 6 -> 0, 2 -> 4
                    adjacency_list[compute_node_index(cell_row, cell_column - 1, 6)].append(compute_node_index(cell_row, cell_column + 1, 0))
                    adjacency_list[compute_node_index(cell_row, cell_column - 1, 2)].append(compute_node_index(cell_row, cell_column + 1, 4))
                    adjacency_list[compute_node_index(cell_row, cell_column + 1, 0)].append(compute_node_index(cell_row, cell_column - 1, 6))
                    adjacency_list[compute_node_index(cell_row, cell_column + 1, 4)].append(compute_node_index(cell_row, cell_column - 1, 2))

search_visited_nodes = [False] * (8 * grid_width * grid_height)

def depth_first_search(start_node):
    search_visited_nodes[start_node] = True
    for destination_node in adjacency_list[start_node]:
        if not search_visited_nodes[destination_node]:
            depth_first_search(destination_node)

depth_first_search(0)

exit_found = False

if grid_height % 2 == 1 and grid_width % 2 == 1:
    for possible_direction in range(8):
        if search_visited_nodes[compute_node_index(grid_height - 1, grid_width - 1, possible_direction)]:
            exit_found = True
    if exit_found:
        print("YES")
        exit()
    else:
        print("NO")
elif grid_height % 2 == 0:
    cell_value = int(grid[grid_height - 1][grid_width - 1])
    if cell_value == 2:
        if (search_visited_nodes[compute_node_index(grid_height - 2, grid_width - 1, 0)] or 
            search_visited_nodes[compute_node_index(grid_height - 2, grid_width - 1, 6)]):
            print("YES")
        else:
            print("NO")
    elif cell_value == 3:
        if (search_visited_nodes[compute_node_index(grid_height - 2, grid_width - 1, 1)] or 
            search_visited_nodes[compute_node_index(grid_height - 2, grid_width - 1, 5)]):
            print("YES")
        else:
            print("NO")
    elif cell_value == 4:
        if (search_visited_nodes[compute_node_index(grid_height - 2, grid_width - 1, 3)] or 
            search_visited_nodes[compute_node_index(grid_height - 2, grid_width - 1, 7)]):
            print("YES")
        else:
            print("NO")
    elif cell_value == 5:
        if (search_visited_nodes[compute_node_index(grid_height - 2, grid_width - 1, 2)] or 
            search_visited_nodes[compute_node_index(grid_height - 2, grid_width - 1, 4)]):
            print("YES")
        else:
            print("NO")
elif grid_width % 2 == 0:
    cell_value = int(grid[grid_height - 1][grid_width - 1])
    if cell_value == 2:
        if (search_visited_nodes[compute_node_index(grid_height - 1, grid_width - 2, 3)] or 
            search_visited_nodes[compute_node_index(grid_height - 1, grid_width - 2, 5)]):
            print("YES")
        else:
            print("NO")
    elif cell_value == 3:
        if (search_visited_nodes[compute_node_index(grid_height - 1, grid_width - 2, 0)] or 
            search_visited_nodes[compute_node_index(grid_height - 1, grid_width - 2, 4)]):
            print("YES")
        else:
            print("NO")
    elif cell_value == 4:
        if (search_visited_nodes[compute_node_index(grid_height - 1, grid_width - 2, 2)] or 
            search_visited_nodes[compute_node_index(grid_height - 1, grid_width - 2, 6)]):
            print("YES")
        else:
            print("NO")
    elif cell_value == 5:
        if (search_visited_nodes[compute_node_index(grid_height - 1, grid_width - 2, 1)] or 
            search_visited_nodes[compute_node_index(grid_height - 1, grid_width - 2, 7)]):
            print("YES")
        else:
            print("NO")
else:
    print("NO")