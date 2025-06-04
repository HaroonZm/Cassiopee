rows_count, cols_count, marks_count = map(int, input().split())
from bisect import bisect_left, bisect_right

marked_cells_list = []
for _ in range(marks_count):
    cell_row, cell_col = map(int, input().split())
    cell_row -= 1
    cell_col -= 1
    marked_cells_list.append([cell_row, cell_col])

marked_cells_list.sort()
result_counts = [0 for _ in range(10)]
subgrid_occurrences_dict = {}

for marked_cell in marked_cells_list:
    for subgrid_row_offset in [-2, -1, 0]:
        for subgrid_col_offset in [-2, -1, 0]:
            anchor_row = marked_cell[0] + subgrid_row_offset
            anchor_col = marked_cell[1] + subgrid_col_offset
            if anchor_row < 0 or anchor_col < 0 or anchor_row + 2 >= rows_count or anchor_col + 2 >= cols_count:
                continue
            subgrid_key = str(anchor_row) + "_" + str(anchor_col)
            try:
                subgrid_occurrences_dict[subgrid_key] += 1
            except KeyError:
                subgrid_occurrences_dict[subgrid_key] = 1

total_subgrids = (rows_count - 2) * (cols_count - 2)
remaining_subgrids = total_subgrids

for num_marks in subgrid_occurrences_dict.values():
    result_counts[num_marks] += 1
    remaining_subgrids -= 1

result_counts[0] = remaining_subgrids

for count in result_counts:
    print(count)