def main():
    num_rectangles, threshold = map(int, input().split())

    rectangles = []
    x_coords = []
    y_coords = []
    d_coords = []

    for _ in range(num_rectangles):
        x_start, y_start, d_start, x_end, y_end, d_end = map(int, input().split())
        rectangles.append((x_start, y_start, d_start, x_end, y_end, d_end))
        x_coords.extend([x_start, x_end])
        y_coords.extend([y_start, y_end])
        d_coords.extend([d_start, d_end])

    unique_x_coords = sorted(set(x_coords))
    unique_y_coords = sorted(set(y_coords))
    unique_d_coords = sorted(set(d_coords))

    x_coord_to_index = {value: index for index, value in enumerate(unique_x_coords)}
    y_coord_to_index = {value: index for index, value in enumerate(unique_y_coords)}
    d_coord_to_index = {value: index for index, value in enumerate(unique_d_coords)}

    coverage_map = [[[0] * len(unique_d_coords) for _ in unique_y_coords] for _ in unique_x_coords]

    for rect in rectangles:
        x_start_idx = x_coord_to_index[rect[0]]
        y_start_idx = y_coord_to_index[rect[1]]
        d_start_idx = d_coord_to_index[rect[2]]
        x_end_idx = x_coord_to_index[rect[3]]
        y_end_idx = y_coord_to_index[rect[4]]
        d_end_idx = d_coord_to_index[rect[5]]

        for x_idx in range(x_start_idx, x_end_idx):
            for y_idx in range(y_start_idx, y_end_idx):
                for d_idx in range(d_start_idx, d_end_idx):
                    coverage_map[x_idx][y_idx][d_idx] += 1

    total_volume = 0
    for x_idx in range(len(unique_x_coords) - 1):
        x_start_val = unique_x_coords[x_idx]
        x_end_val = unique_x_coords[x_idx + 1]
        for y_idx in range(len(unique_y_coords) - 1):
            y_start_val = unique_y_coords[y_idx]
            y_end_val = unique_y_coords[y_idx + 1]
            for d_idx in range(len(unique_d_coords) - 1):
                d_start_val = unique_d_coords[d_idx]
                d_end_val = unique_d_coords[d_idx + 1]

                if coverage_map[x_idx][y_idx][d_idx] >= threshold:
                    volume = (x_end_val - x_start_val) * (y_end_val - y_start_val) * (d_end_val - d_start_val)
                    total_volume += volume

    print(total_volume)

main()