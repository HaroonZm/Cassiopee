class TwoDimensionalBinaryIndexedTree:

    def __init__(self, num_rows, num_columns):
        self.total_rows = num_rows
        self.total_columns = num_columns
        self.tree_data = [{} for _ in range(num_rows + 1)]

    def prefix_sum(self, row_index, column_index):
        accumulated_sum = 0
        data_reference = self.tree_data
        current_row = row_index
        while current_row > 0:
            row_dict = data_reference[current_row]
            current_column = column_index
            while current_column > 0:
                accumulated_sum += row_dict.get(current_column, 0)
                current_column -= current_column & -current_column
            current_row -= current_row & -current_row
        return accumulated_sum

    def add_value(self, row_index, column_index, value_to_add):
        data_reference = self.tree_data
        max_column = self.total_columns
        max_row = self.total_rows
        current_row = row_index
        while current_row <= max_row:
            row_dict = data_reference[current_row]
            current_column = column_index
            while current_column <= max_column:
                row_dict[current_column] = row_dict.get(current_column, 0) + value_to_add
                current_column += current_column & -current_column
            current_row += current_row & -current_row

    def range_sum(self, row_start_inclusive, row_end_exclusive, column_start_inclusive, column_end_exclusive):
        return (
            self.prefix_sum(row_end_exclusive, column_end_exclusive)
            - self.prefix_sum(row_end_exclusive, column_start_inclusive)
            - self.prefix_sum(row_start_inclusive, column_end_exclusive)
            + self.prefix_sum(row_start_inclusive, column_start_inclusive)
        )


import sys
from collections import deque

input_row_count, input_column_count, time_to_bake, number_of_queries = map(int, input().split())

ready_bread_tree = TwoDimensionalBinaryIndexedTree(input_row_count + 1, input_column_count + 1)
edible_bread_tree = TwoDimensionalBinaryIndexedTree(input_row_count + 1, input_column_count + 1)

baking_queue = deque()

for current_query_index in range(number_of_queries):
    query_parameters = list(map(int, input().split()))

    # Advance baking process: move breads to edible if their baking time is over
    while baking_queue and baking_queue[0][0] + time_to_bake <= query_parameters[0]:
        baking_start_time, baking_row_coord, baking_col_coord = baking_queue.popleft()
        edible_bread_tree.add_value(baking_row_coord, baking_col_coord, 1)

    query_type = query_parameters[1]
    if query_type == 0:
        candidate_row, candidate_column = query_parameters[2:]
        breads_ready_in_cell = ready_bread_tree.range_sum(candidate_row - 1, candidate_row, candidate_column - 1, candidate_column)
        if breads_ready_in_cell == 0:
            ready_bread_tree.add_value(candidate_row, candidate_column, 1)
            baking_queue.append((query_parameters[0], candidate_row, candidate_column))

    elif query_type == 1:
        target_row, target_column = query_parameters[2:]
        breads_edible_in_cell = edible_bread_tree.range_sum(target_row - 1, target_row, target_column - 1, target_column)
        if breads_edible_in_cell == 1:
            ready_bread_tree.add_value(target_row, target_column, -1)
            edible_bread_tree.add_value(target_row, target_column, -1)

    elif query_type == 2:
        query_row_start, query_column_start, query_row_end, query_column_end = query_parameters[2:]
        total_edible_breads = edible_bread_tree.range_sum(
            query_row_start - 1, query_row_end, query_column_start - 1, query_column_end
        )
        total_ready_breads = ready_bread_tree.range_sum(
            query_row_start - 1, query_row_end, query_column_start - 1, query_column_end
        )
        total_breads_currently_baking = total_ready_breads - total_edible_breads
        print(f"{total_edible_breads} {total_breads_currently_baking}")