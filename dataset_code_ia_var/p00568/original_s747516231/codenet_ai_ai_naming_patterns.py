grid_height, grid_width = map(int, input().split())

grid_values = [[0 for col_idx in range(grid_width)] for row_idx in range(grid_height)]

for row_idx in range(grid_height):
    grid_values[row_idx] = list(map(int, input().split()))

min_costs = [[[float('inf') for step_idx in range(grid_height * grid_width)] for row_idx in range(grid_height)] for col_idx in range(grid_width)]
min_costs[0][0][0] = 0

for step_idx in range(1, grid_width * grid_height):
    for col_idx in range(grid_width):
        if col_idx > step_idx:
            break
        for row_idx in range(grid_height):
            if col_idx + row_idx > step_idx:
                break

            # Move left
            if col_idx != 0:
                candidate_cost = min_costs[col_idx][row_idx][step_idx - 1] + ((step_idx - 1) * 2 + 1) * grid_values[row_idx][col_idx - 1]
                if min_costs[col_idx - 1][row_idx][step_idx] > candidate_cost:
                    min_costs[col_idx - 1][row_idx][step_idx] = candidate_cost

            # Move right
            if col_idx != (grid_width - 1):
                candidate_cost = min_costs[col_idx][row_idx][step_idx - 1] + ((step_idx - 1) * 2 + 1) * grid_values[row_idx][col_idx + 1]
                if min_costs[col_idx + 1][row_idx][step_idx] > candidate_cost:
                    min_costs[col_idx + 1][row_idx][step_idx] = candidate_cost

            # Move up
            if row_idx != 0:
                candidate_cost = min_costs[col_idx][row_idx][step_idx - 1] + ((step_idx - 1) * 2 + 1) * grid_values[row_idx - 1][col_idx]
                if min_costs[col_idx][row_idx - 1][step_idx] > candidate_cost:
                    min_costs[col_idx][row_idx - 1][step_idx] = candidate_cost

            # Move down
            if row_idx != (grid_height - 1):
                candidate_cost = min_costs[col_idx][row_idx][step_idx - 1] + ((step_idx - 1) * 2 + 1) * grid_values[row_idx + 1][col_idx]
                if min_costs[col_idx][row_idx + 1][step_idx] > candidate_cost:
                    min_costs[col_idx][row_idx + 1][step_idx] = candidate_cost

print(min(min_costs[grid_width - 1][grid_height - 1]))