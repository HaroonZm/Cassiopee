grid_size = int(input())
query_count = int(input())
for query_index in range(query_count):
    coord_x, coord_y = map(int, input().split())
    min_distance = min(coord_x, coord_y, grid_size - coord_x + 1, grid_size - coord_y + 1)
    mod_result = min_distance % 3
    if mod_result == 0:
        print(3)
    elif mod_result == 1:
        print(1)
    else:
        print(2)