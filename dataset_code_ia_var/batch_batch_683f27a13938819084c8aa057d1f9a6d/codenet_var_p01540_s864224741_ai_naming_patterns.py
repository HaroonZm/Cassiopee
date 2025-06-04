from bisect import bisect_left

def process_treasure_hunt():
    treasure_count, query_count = map(int, input().split())
    treasure_list = []

    x_coordinate_set = set()
    y_coordinate_set = set()

    for _ in range(treasure_count):
        treasure_x, treasure_y = map(int, input().split())
        treasure_list.append((treasure_x, treasure_y))
        x_coordinate_set.add(treasure_x)
        y_coordinate_set.add(treasure_y)

    x_coordinate_list = sorted(list(x_coordinate_set))
    y_coordinate_list = sorted(list(y_coordinate_set))
    x_index_map = {x_value: x_idx for x_idx, x_value in enumerate(x_coordinate_list)}
    y_index_map = {y_value: y_idx for y_idx, y_value in enumerate(y_coordinate_list)}

    x_total = len(x_coordinate_list)
    y_total = len(y_coordinate_list)
    grid_count = [[0] * (x_total + 1) for _ in range(y_total + 1)]

    for treasure_x, treasure_y in treasure_list:
        y_comp_idx = y_index_map[treasure_y] + 1
        x_comp_idx = x_index_map[treasure_x] + 1
        grid_count[y_comp_idx][x_comp_idx] += 1

    for y_pos in range(1, y_total + 1):
        row_accumulate = 0
        for x_pos in range(1, x_total + 1):
            row_accumulate += grid_count[y_pos][x_pos]
            grid_count[y_pos][x_pos] = row_accumulate + grid_count[y_pos-1][x_pos]

    for _ in range(query_count):
        query_x1, query_y1, query_x2, query_y2 = map(int, input().split())
        x1_comp_idx = bisect_left(x_coordinate_list, query_x1)
        x2_comp_idx = bisect_left(x_coordinate_list, query_x2)
        y1_comp_idx = bisect_left(y_coordinate_list, query_y1)
        y2_comp_idx = bisect_left(y_coordinate_list, query_y2)

        if x2_comp_idx < x_total and x_coordinate_list[x2_comp_idx] == query_x2:
            x2_comp_idx += 1
        if y2_comp_idx < y_total and y_coordinate_list[y2_comp_idx] == query_y2:
            y2_comp_idx += 1

        region_treasure_sum = (
            grid_count[y2_comp_idx][x2_comp_idx]
            - grid_count[y2_comp_idx][x1_comp_idx]
            - grid_count[y1_comp_idx][x2_comp_idx]
            + grid_count[y1_comp_idx][x1_comp_idx]
        )
        print(region_treasure_sum)

if __name__ == "__main__":
    process_treasure_hunt()