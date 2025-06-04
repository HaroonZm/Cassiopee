import heapq
import itertools

def process_solution():
    min_heap = [(0, row_idx, col_idx) for row_idx, col_idx in itertools.product(range_var_m, range_var_n)
                if not (0 < row_idx < value_m_minus1 and 0 < col_idx < value_n_minus1)]
    heapq.heapify(min_heap)
    while min_heap:
        current_cost, current_row, current_col = heapq.heappop(min_heap)
        if grid_field[current_row][current_col] == "&":
            return current_cost
        if cost_memo[current_row][current_col] <= current_cost:
            continue
        cost_memo[current_row][current_col] = current_cost
        for move_delta_x, move_delta_y in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            neighbor_row = current_row + move_delta_y
            neighbor_col = current_col + move_delta_x
            if 0 <= neighbor_row < value_m and 0 <= neighbor_col < value_n:
                if grid_field[neighbor_row][neighbor_col] != "#" and grid_field[current_row][current_col] == "#":
                    heapq.heappush(min_heap, (current_cost + 1, neighbor_row, neighbor_col))
                else:
                    heapq.heappush(min_heap, (current_cost, neighbor_row, neighbor_col))

while True:
    value_n, value_m = map(int, raw_input().split())
    if value_n == 0 and value_m == 0:
        break
    value_n_minus1 = value_n - 1
    value_m_minus1 = value_m - 1
    range_var_n = xrange(value_n)
    range_var_m = xrange(value_m)
    cost_memo = [[1 << 20 for _ in range_var_n] for _ in range_var_m]
    grid_field = [raw_input() for _ in range_var_m]
    print process_solution()