INFINITY = 10**20
row_count, col_count = map(int, input().split())
grid_rows = []
row_color_counts = {}
for row_index in range(row_count):
    row_chars = list(str(input()))
    grid_rows.append(row_chars)
    color_counts = []
    color_counts.append(row_chars.count('W'))
    color_counts.append(row_chars.count('B'))
    color_counts.append(row_chars.count('R'))
    row_color_counts[row_index] = color_counts
min_changes = INFINITY
for white_end in range(row_count - 2):
    white_changes = 0
    for row_idx in range(white_end + 1):
        white_changes += (row_color_counts[row_idx][1] + row_color_counts[row_idx][2])
    for blue_end in range(white_end + 1, row_count - 1):
        blue_changes = 0
        red_changes = 0
        for row_idx in range(white_end + 1, blue_end + 1):
            blue_changes += (row_color_counts[row_idx][0] + row_color_counts[row_idx][2])
        for row_idx in range(blue_end + 1, row_count):
            red_changes += (row_color_counts[row_idx][0] + row_color_counts[row_idx][1])
        min_changes = min(min_changes, (white_changes + blue_changes + red_changes))
print(min_changes)