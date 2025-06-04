import sys
from itertools import permutations
from collections import deque

def read_input_dimensions():
    return map(int, input().split())

def read_map_rows(input_width, input_height):
    border_row = "X" * (input_width + 4)
    map_grid = [border_row] * 2
    for _ in range(input_height):
        map_grid.append("XX" + input() + "XX")
    map_grid += [border_row] * 2
    return map_grid

def collect_positions(map_grid, map_width, map_height):
    pos_start = pos_goal = None
    pos_m_points = []
    pos_holes = []
    for row_idx in range(2, map_height + 2):
        for col_idx in range(2, map_width + 2):
            cell = map_grid[row_idx][col_idx]
            if cell == "S":
                pos_start = (col_idx, row_idx)
            elif cell == "G":
                pos_goal = (col_idx, row_idx)
            elif cell == "M":
                pos_m_points.append((col_idx, row_idx))
            elif cell == "#":
                pos_holes.append((col_idx, row_idx))
    return pos_start, pos_goal, pos_m_points, pos_holes

def generate_move_costs(map_width, map_height, holes_positions):
    cost_map = [[1] * (map_width + 4) for _ in range(map_height + 4)]
    for hole_x, hole_y in holes_positions:
        for dy in range(hole_y - 2, hole_y + 3):
            for dx in range(hole_x - 2, hole_x + 3):
                cost_map[dy][dx] = max(2, cost_map[dy][dx])
        for dy in range(hole_y - 1, hole_y + 2):
            for dx in range(hole_x - 1, hole_x + 2):
                cost_map[dy][dx] = 3
    return cost_map

def compute_shortest_path(map_grid, move_cost_grid, src_x, src_y, map_width, map_height):
    DIRECTION_VECTORS = ((1, 0), (0, -1), (-1, 0), (0, 1))
    IMPASSABLE_COST = 10 ** 20
    path_costs = [[IMPASSABLE_COST] * (map_width + 4) for _ in range(map_height + 4)]
    path_costs[src_y][src_x] = 0
    traversal_queue = deque()
    traversal_queue.append((0, src_x, src_y))
    while traversal_queue:
        curr_score, curr_x, curr_y = traversal_queue.popleft()
        updated_score = curr_score + move_cost_grid[curr_y][curr_x]
        for dx, dy in DIRECTION_VECTORS:
            next_x, next_y = curr_x + dx, curr_y + dy
            if map_grid[next_y][next_x] in {"S", "G", ".", "M"} and updated_score < path_costs[next_y][next_x]:
                path_costs[next_y][next_x] = updated_score
                traversal_queue.append((updated_score, next_x, next_y))
    return path_costs

def build_edges_between_points(m_points, goal_pos, map_grid, move_cost_grid, map_width, map_height):
    adj_edge_costs = []
    gx, gy = goal_pos
    for src_x, src_y in m_points:
        current_path_costs = compute_shortest_path(map_grid, move_cost_grid, src_x, src_y, map_width, map_height)
        point_edge = []
        for dst_x, dst_y in m_points:
            point_edge.append(current_path_costs[dst_y][dst_x])
        point_edge.append(current_path_costs[gy][gx])
        adj_edge_costs.append(point_edge)
    return adj_edge_costs

def main():
    input_width, input_height = read_input_dimensions()
    map_grid = read_map_rows(input_width, input_height)
    pos_start, pos_goal, pos_m_points, pos_holes = collect_positions(map_grid, input_width, input_height)
    move_cost_grid = generate_move_costs(input_width, input_height, pos_holes)

    edge_costs_matrix = build_edges_between_points(
        pos_m_points, pos_goal, map_grid, move_cost_grid, input_width, input_height
    )
    start_costs = compute_shortest_path(
        map_grid, move_cost_grid, pos_start[0], pos_start[1], input_width, input_height
    )
    ans_cost = 10 ** 20
    m_point_count = len(edge_costs_matrix)
    for point_order in permutations(range(m_point_count), m_point_count):
        traversal_sequence = list(point_order)
        seq_cost = 0
        for idx in range(m_point_count - 1):
            seq_cost += edge_costs_matrix[traversal_sequence[idx]][traversal_sequence[idx + 1]]
        first_mx, first_my = pos_m_points[traversal_sequence[0]]
        last_mx, last_my = pos_m_points[traversal_sequence[-1]]
        seq_cost += start_costs[first_my][first_mx]
        seq_cost += edge_costs_matrix[traversal_sequence[-1]][-1]
        ans_cost = min(ans_cost, seq_cost)
    print(ans_cost)

if __name__ == "__main__":
    main()