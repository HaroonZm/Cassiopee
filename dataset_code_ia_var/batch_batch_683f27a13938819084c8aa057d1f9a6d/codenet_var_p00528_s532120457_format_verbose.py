from heapq import heappush, heappop

number_of_rows, number_of_columns, number_of_special_cells = map(int, input().split())

special_cells_in_row = [[] for row_index in range(number_of_rows)]
special_cells_in_column = [[] for column_index in range(number_of_columns)]

for special_cell_id in range(number_of_special_cells):
    input_row, input_column = map(int, input().split())
    row_index = input_row - 1
    column_index = input_column - 1
    special_cells_in_row[row_index].append((column_index, special_cell_id))
    special_cells_in_column[column_index].append((row_index, special_cell_id))

adjacency_graph_within_row = [[] for special_cell_id in range(number_of_special_cells)]
adjacency_graph_within_column = [[] for special_cell_id in range(number_of_special_cells)]

for row_index in range(number_of_rows):
    cells_in_this_row = special_cells_in_row[row_index]
    if cells_in_this_row:
        cells_in_this_row.sort()
        previous_cell = cells_in_this_row[0]
        for current_cell in cells_in_this_row[1:]:
            column_distance = current_cell[0] - previous_cell[0]
            adjacency_graph_within_row[previous_cell[1]].append((current_cell[1], column_distance))
            adjacency_graph_within_row[current_cell[1]].append((previous_cell[1], column_distance))
            previous_cell = current_cell

for column_index in range(number_of_columns):
    cells_in_this_column = special_cells_in_column[column_index]
    if cells_in_this_column:
        cells_in_this_column.sort()
        previous_cell = cells_in_this_column[0]
        for current_cell in cells_in_this_column[1:]:
            row_distance = current_cell[0] - previous_cell[0]
            adjacency_graph_within_column[previous_cell[1]].append((current_cell[1], row_distance))
            adjacency_graph_within_column[current_cell[1]].append((previous_cell[1], row_distance))
            previous_cell = current_cell

INFINITY_COST = 10 ** 18

priority_queue = []
minimum_cost_from_row_traversal = [INFINITY_COST] * number_of_special_cells
minimum_cost_from_column_traversal = [INFINITY_COST] * number_of_special_cells

if special_cells_in_row[0]:
    first_column_index, first_special_cell_id = special_cells_in_row[0][0]
    priority_queue.append((first_column_index, 0, first_special_cell_id))

while priority_queue:
    current_total_cost, current_traversal_mode, current_special_cell_id = heappop(priority_queue)
    if current_traversal_mode == 0:
        if minimum_cost_from_row_traversal[current_special_cell_id] < current_total_cost:
            continue
        for neighbor_special_cell_id, distance in adjacency_graph_within_row[current_special_cell_id]:
            new_cost = current_total_cost + distance
            if new_cost < minimum_cost_from_row_traversal[neighbor_special_cell_id]:
                minimum_cost_from_row_traversal[neighbor_special_cell_id] = new_cost
                heappush(priority_queue, (new_cost, 0, neighbor_special_cell_id))
        teleportation_cost = current_total_cost + 1
        if teleportation_cost < minimum_cost_from_column_traversal[current_special_cell_id]:
            minimum_cost_from_column_traversal[current_special_cell_id] = teleportation_cost
            heappush(priority_queue, (teleportation_cost, 1, current_special_cell_id))
    else:
        if minimum_cost_from_column_traversal[current_special_cell_id] < current_total_cost:
            continue
        for neighbor_special_cell_id, distance in adjacency_graph_within_column[current_special_cell_id]:
            new_cost = current_total_cost + distance
            if new_cost < minimum_cost_from_column_traversal[neighbor_special_cell_id]:
                minimum_cost_from_column_traversal[neighbor_special_cell_id] = new_cost
                heappush(priority_queue, (new_cost, 1, neighbor_special_cell_id))
        teleportation_cost = current_total_cost + 1
        if teleportation_cost < minimum_cost_from_row_traversal[current_special_cell_id]:
            minimum_cost_from_row_traversal[current_special_cell_id] = teleportation_cost
            heappush(priority_queue, (teleportation_cost, 0, current_special_cell_id))

minimum_total_cost = INFINITY_COST

if special_cells_in_row[number_of_rows - 1]:
    last_column_index_in_last_row, last_special_cell_id_in_last_row = special_cells_in_row[number_of_rows - 1][-1]
    total_cost_via_row = minimum_cost_from_row_traversal[last_special_cell_id_in_last_row] + (number_of_columns - 1 - last_column_index_in_last_row)
    minimum_total_cost = min(minimum_total_cost, total_cost_via_row)

if special_cells_in_column[number_of_columns - 1]:
    last_row_index_in_last_column, last_special_cell_id_in_last_column = special_cells_in_column[number_of_columns - 1][-1]
    total_cost_via_column = minimum_cost_from_column_traversal[last_special_cell_id_in_last_column] + (number_of_rows - 1 - last_row_index_in_last_column)
    minimum_total_cost = min(minimum_total_cost, total_cost_via_column)

if minimum_total_cost < INFINITY_COST:
    print(minimum_total_cost)
else:
    print(-1)