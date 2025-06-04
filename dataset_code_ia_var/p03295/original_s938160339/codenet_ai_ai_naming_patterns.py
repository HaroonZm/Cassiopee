num_rows, num_columns = map(int, input().split())
matrix_entries = []
for row_index in range(num_columns):
    matrix_entries.append([int(entry) for entry in input().split()])
matrix_entries.sort(key=lambda entry: (entry[0], entry[1]))
interval_starts = [0] * num_rows
interval_ends = [0] * num_rows
interval_index = 0
interval_count = 0
for entry_index in range(num_columns):
    if entry_index == 0:
        interval_starts[interval_index] = matrix_entries[entry_index][0]
        interval_ends[interval_index] = matrix_entries[entry_index][1] - 1
    else:
        if matrix_entries[entry_index][0] != matrix_entries[entry_index - 1][0]:
            interval_index += 1
            interval_starts[interval_index] = matrix_entries[entry_index][0]
            interval_ends[interval_index] = matrix_entries[entry_index][1] - 1
            if interval_ends[interval_index - 1] < interval_starts[interval_index]:
                interval_count += 1
            else:
                if interval_starts[interval_index] < interval_starts[interval_index - 1]:
                    interval_starts[interval_index] = interval_starts[interval_index - 1]
                if interval_ends[interval_index] > interval_ends[interval_index - 1]:
                    interval_ends[interval_index] = interval_ends[interval_index - 1]
interval_count += 1
print(interval_count)