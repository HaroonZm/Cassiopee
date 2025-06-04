import heapq
import os
import sys

def input_readline():
    return sys.stdin.readline().rstrip()

def parse_single_int():
    return int(input_readline())

def parse_int_list():
    return [int(elem) for elem in input_readline().split()]

def log_debug(*args, sep=' ', end='\n'):
    if IS_DEBUG_MODE:
        print(*args, sep=sep, end=end)

def main_entrypoint():
    grid_height, grid_width = parse_int_list()
    grid_matrix = [parse_int_list() for _ in range(grid_height)]
    print(find_minimum_cost(grid_height, grid_width, grid_matrix))

def find_minimum_cost(grid_height, grid_width, grid_matrix):
    max_distance = grid_height * grid_width
    distance_matrix = [[[None] * (max_distance + 1) for _ in range(grid_width)] for _ in range(grid_height)]

    minimum_cost = 2 ** 63
    priority_queue = []
    heapq.heappush(priority_queue, (0, 0, 0, 0))  # (cost, distance, x_pos, y_pos)
    
    while priority_queue:
        current_cost, current_distance, pos_x, pos_y = heapq.heappop(priority_queue)
        if (pos_x, pos_y) == (grid_width - 1, grid_height - 1):
            minimum_cost = min(minimum_cost, current_cost - current_distance)
        if distance_matrix[pos_y][pos_x][current_distance] is not None:
            continue
        for distance_step in range(current_distance, max_distance + 1):
            if distance_matrix[pos_y][pos_x][distance_step] is not None:
                break
            distance_matrix[pos_y][pos_x][distance_step] = current_cost
        if current_cost - max_distance >= minimum_cost:
            break
        for delta_x, delta_y in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            neighbor_x = pos_x + delta_x
            neighbor_y = pos_y + delta_y
            if neighbor_x < 0 or neighbor_x >= grid_width or neighbor_y < 0 or neighbor_y >= grid_height:
                continue
            next_distance = current_distance + 1
            next_cost = current_cost + grid_matrix[neighbor_y][neighbor_x] * (1 + current_distance * 2) + 1
            if next_distance > max_distance:
                continue
            if distance_matrix[neighbor_y][neighbor_x][next_distance] is None:
                heapq.heappush(priority_queue, (next_cost, next_distance, neighbor_x, neighbor_y))

    return minimum_cost

IS_DEBUG_MODE = 'DEBUG' in os.environ

if __name__ == '__main__':
    main_entrypoint()