row_count, col_count = map(int, input().split())
white_row_counts = []
blue_row_counts = []
red_row_counts = []
for row_index in range(row_count):
    row_str = input()
    white_row_counts.append(col_count - row_str.count("W"))
    blue_row_counts.append(col_count - row_str.count("B"))
    red_row_counts.append(col_count - row_str.count("R"))
min_total_changes = float('inf')
for white_end_row in range(1, row_count - 1):
    for blue_end_row in range(white_end_row, row_count - 1):
        total_changes = (
            sum(white_row_counts[:white_end_row])
            + sum(blue_row_counts[white_end_row:blue_end_row + 1])
            + sum(red_row_counts[blue_end_row + 1:])
        )
        if total_changes < min_total_changes:
            min_total_changes = total_changes
print(min_total_changes)