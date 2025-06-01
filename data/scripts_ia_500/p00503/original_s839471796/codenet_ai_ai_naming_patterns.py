num_points, threshold = map(int, input().split())

points_list = []
x_coords = []
y_coords = []
d_coords = []

for _ in range(num_points):
    x_start, y_start, d_start, x_end, y_end, d_end = map(int, input().split())
    points_list.append((x_start, y_start, d_start, x_end, y_end, d_end))
    x_coords.extend([x_start, x_end])
    y_coords.extend([y_start, y_end])
    d_coords.extend([d_start, d_end])

unique_x_coords = sorted(set(x_coords))
unique_y_coords = sorted(set(y_coords))
unique_d_coords = sorted(set(d_coords))

x_index_map = {value: index for index, value in enumerate(unique_x_coords)}
y_index_map = {value: index for index, value in enumerate(unique_y_coords)}
d_index_map = {value: index for index, value in enumerate(unique_d_coords)}

count_map = [[[0 for _ in range(len(unique_d_coords))] for _ in range(len(unique_y_coords))] for _ in range(len(unique_x_coords))]

for x_start, y_start, d_start, x_end, y_end, d_end in points_list:
    x_start_idx = x_index_map[x_start]
    y_start_idx = y_index_map[y_start]
    d_start_idx = d_index_map[d_start]
    x_end_idx = x_index_map[x_end]
    y_end_idx = y_index_map[y_end]
    d_end_idx = d_index_map[d_end]
    for x_idx in range(x_start_idx, x_end_idx):
        for y_idx in range(y_start_idx, y_end_idx):
            for d_idx in range(d_start_idx, d_end_idx):
                count_map[x_idx][y_idx][d_idx] += 1

total_volume = 0
for x_idx in range(len(unique_x_coords) - 1):
    for y_idx in range(len(unique_y_coords) - 1):
        for d_idx in range(len(unique_d_coords) - 1):
            if count_map[x_idx][y_idx][d_idx] >= threshold:
                delta_x = unique_x_coords[x_idx + 1] - unique_x_coords[x_idx]
                delta_y = unique_y_coords[y_idx + 1] - unique_y_coords[y_idx]
                delta_d = unique_d_coords[d_idx + 1] - unique_d_coords[d_idx]
                total_volume += delta_x * delta_y * delta_d

print(total_volume)