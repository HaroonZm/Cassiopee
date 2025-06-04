grid_height, grid_width = map(int, input().split())

input_grid = [input() for _ in range(grid_height)]

can_reach_target = [[0] * grid_width for _ in range(grid_height)]
can_reach_target[0][0] = 1

cells_to_visit = [(0, 0)]

while cells_to_visit:
    current_row, current_col = cells_to_visit.pop()

    possible_neighbors = [
        (current_row + 1, current_col),
        (current_row - 1, current_col),
        (current_row, current_col + 1),
        (current_row, current_col - 1)
    ]

    for neighbor_row, neighbor_col in possible_neighbors:

        within_row_bounds = 0 <= neighbor_row < grid_height
        within_col_bounds = 0 <= neighbor_col < grid_width
        not_visited = can_reach_target[neighbor_row][neighbor_col] == 0

        if within_row_bounds and within_col_bounds and not_visited:

            row_modulus = neighbor_row % 4
            col_modulus = neighbor_col % 4
            cell_value = input_grid[neighbor_row][neighbor_col]

            if row_modulus == 0:
                if col_modulus == 0 and cell_value == "6":
                    can_reach_target[neighbor_row][neighbor_col] = 1
                    cells_to_visit.append((neighbor_row, neighbor_col))
                if col_modulus == 1 and cell_value == "3":
                    can_reach_target[neighbor_row][neighbor_col] = 1
                    cells_to_visit.append((neighbor_row, neighbor_col))
                if col_modulus == 2 and cell_value == "1":
                    can_reach_target[neighbor_row][neighbor_col] = 1
                    cells_to_visit.append((neighbor_row, neighbor_col))
                if col_modulus == 3 and cell_value == "4":
                    can_reach_target[neighbor_row][neighbor_col] = 1
                    cells_to_visit.append((neighbor_row, neighbor_col))

            if row_modulus == 2:
                if col_modulus == 0 and cell_value == "1":
                    can_reach_target[neighbor_row][neighbor_col] = 1
                    cells_to_visit.append((neighbor_row, neighbor_col))
                if col_modulus == 1 and cell_value == "3":
                    can_reach_target[neighbor_row][neighbor_col] = 1
                    cells_to_visit.append((neighbor_row, neighbor_col))
                if col_modulus == 2 and cell_value == "6":
                    can_reach_target[neighbor_row][neighbor_col] = 1
                    cells_to_visit.append((neighbor_row, neighbor_col))
                if col_modulus == 3 and cell_value == "4":
                    can_reach_target[neighbor_row][neighbor_col] = 1
                    cells_to_visit.append((neighbor_row, neighbor_col))

            if row_modulus == 1:
                if col_modulus == 0 and cell_value == "2":
                    can_reach_target[neighbor_row][neighbor_col] = 1
                    cells_to_visit.append((neighbor_row, neighbor_col))
                if col_modulus == 2 and cell_value == "2":
                    can_reach_target[neighbor_row][neighbor_col] = 1
                    cells_to_visit.append((neighbor_row, neighbor_col))

            if row_modulus == 3:
                if col_modulus == 0 and cell_value == "5":
                    can_reach_target[neighbor_row][neighbor_col] = 1
                    cells_to_visit.append((neighbor_row, neighbor_col))
                if col_modulus == 2 and cell_value == "5":
                    can_reach_target[neighbor_row][neighbor_col] = 1
                    cells_to_visit.append((neighbor_row, neighbor_col))

if can_reach_target[grid_height - 1][grid_width - 1] == 1:
    print("YES")
else:
    print("NO")