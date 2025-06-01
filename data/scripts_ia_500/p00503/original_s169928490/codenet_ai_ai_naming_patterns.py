input_count, threshold_k = map(int, input().split())
points_list = []
x_values = []
y_values = []
d_values = []

for _ in range(input_count):
    x_start, y_start, d_start, x_end, y_end, d_end = map(int, input().split())
    points_list.append((x_start, y_start, d_start, x_end, y_end, d_end))
    x_values.append(x_start)
    x_values.append(x_end)
    y_values.append(y_start)
    y_values.append(y_end)
    d_values.append(d_start)
    d_values.append(d_end)

x_values = list(set(x_values))
y_values = list(set(y_values))
d_values = list(set(d_values))

x_values.sort()
y_values.sort()
d_values.sort()

len_x = len(x_values)
len_y = len(y_values)
len_d = len(d_values)

x_index_map = dict(reversed(t) for t in enumerate(x_values))
y_index_map = dict(reversed(t) for t in enumerate(y_values))
d_index_map = dict(reversed(t) for t in enumerate(d_values))

frequency_map = [[[0] * len_d for _ in range(len_y)] for _ in range(len_x)]

for point in points_list:
    x_start, y_start, d_start, x_end, y_end, d_end = point
    x_start_idx = x_index_map[x_start]
    y_start_idx = y_index_map[y_start]
    d_start_idx = d_index_map[d_start]
    x_end_idx = x_index_map[x_end]
    y_end_idx = y_index_map[y_end]
    d_end_idx = d_index_map[d_end]
    for xi in range(x_start_idx, x_end_idx):
        for yi in range(y_start_idx, y_end_idx):
            for di in range(d_start_idx, d_end_idx):
                frequency_map[xi][yi][di] += 1

accumulated_answer = 0
for xi in range(len_x - 1):
    x_val = x_values[xi]
    x_val_next = x_values[xi + 1]
    x_i_mapped = x_index_map[x_val]
    for yi in range(len_y - 1):
        y_val = y_values[yi]
        y_val_next = y_values[yi + 1]
        y_i_mapped = y_index_map[y_val]
        for di in range(len_d - 1):
            d_val = d_values[di]
            d_val_next = d_values[di + 1]
            d_i_mapped = d_index_map[d_val]
            if frequency_map[x_i_mapped][y_i_mapped][d_i_mapped] >= threshold_k:
                volume = (x_val_next - x_val) * (y_val_next - y_val) * (d_val_next - d_val)
                accumulated_answer += volume

print(accumulated_answer)