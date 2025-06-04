import sys
from collections import deque

stdin_read = sys.stdin.readline
stdout_write = sys.stdout.write

def main_solution():
    height, width, row, col = map(int, stdin_read().split())
    row -= 1
    col -= 1
    if height == 0 and width == 0:
        return False

    node_count = height * width
    super_node = node_count
    adjacency_group_0 = [[] for _ in range(node_count + 1)]
    adjacency_group_1 = [[] for _ in range(node_count + 1)]

    for current_row in range(height):
        cell_values = list(map(int, stdin_read().split()))
        node_offset = current_row * width

        if current_row > 0:
            for cell_index in range(width):
                upper_node = node_offset + cell_index - width
                current_node = node_offset + cell_index
                if cell_values[cell_index] == 1:
                    adjacency_group_1[current_node].append(upper_node)
                    adjacency_group_1[upper_node].append(current_node)
                else:
                    adjacency_group_0[current_node].append(upper_node)
                    adjacency_group_0[upper_node].append(current_node)
        else:
            for cell_index in range(width):
                current_node = cell_index
                if cell_values[cell_index] == 1:
                    adjacency_group_1[current_node].append(super_node)
                    adjacency_group_1[super_node].append(current_node)
                else:
                    adjacency_group_0[current_node].append(super_node)
                    adjacency_group_0[super_node].append(current_node)

        border_values = list(map(int, stdin_read().split()))
        for border_index in range(width - 1):
            left_node = node_offset + border_index
            right_node = node_offset + border_index + 1
            if border_values[border_index + 1] == 1:
                adjacency_group_1[left_node].append(right_node)
                adjacency_group_1[right_node].append(left_node)
            else:
                adjacency_group_0[left_node].append(right_node)
                adjacency_group_0[right_node].append(left_node)

        if border_values[0] == 1:
            adjacency_group_1[node_offset].append(super_node)
            adjacency_group_1[super_node].append(node_offset)
        else:
            adjacency_group_0[node_offset].append(super_node)
            adjacency_group_0[super_node].append(node_offset)

        if border_values[width] == 1:
            adjacency_group_1[node_offset + width - 1].append(super_node)
            adjacency_group_1[super_node].append(node_offset + width - 1)
        else:
            adjacency_group_0[node_offset + width - 1].append(super_node)
            adjacency_group_0[super_node].append(node_offset + width - 1)

    last_border_values = list(map(int, stdin_read().split()))
    last_row_offset = (height - 1) * width
    for cell_index in range(width):
        current_node = last_row_offset + cell_index
        if last_border_values[cell_index] == 1:
            adjacency_group_1[current_node].append(super_node)
            adjacency_group_1[super_node].append(current_node)
        else:
            adjacency_group_0[current_node].append(super_node)
            adjacency_group_0[super_node].append(current_node)

    visited_group_0 = [0] * (node_count + 1)
    visited_group_1 = [0] * (node_count + 1)
    visited_group_0[super_node] = 1
    visited_group_1[super_node] = 1

    bfs_queue = deque([super_node])
    while bfs_queue:
        current_vertex = bfs_queue.popleft()
        for neighbor in adjacency_group_0[current_vertex]:
            if visited_group_0[neighbor]:
                continue
            if visited_group_1[neighbor]:
                bfs_queue.append(neighbor)
            visited_group_0[neighbor] = 1
        for neighbor in adjacency_group_1[current_vertex]:
            if visited_group_1[neighbor]:
                continue
            if visited_group_0[neighbor]:
                bfs_queue.append(neighbor)
            visited_group_1[neighbor] = 1

    target_node = row * width + col
    if visited_group_0[target_node]:
        stdout_write("Yes\n")
    else:
        stdout_write("No\n")

    return True

while main_solution():
    pass