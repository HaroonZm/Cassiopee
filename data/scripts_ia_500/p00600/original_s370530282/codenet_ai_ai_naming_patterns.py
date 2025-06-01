while True:
    station_count, distance_count = [int(value) for value in input().split()]
    if station_count == 0:
        break
    min_distances = [999 for _ in range(distance_count)]
    for station_index in range(station_count):
        distance_list = [int(value) for value in input().split()]
        for dist_index in range(distance_count):
            if distance_list[dist_index] != 0:
                min_distances[dist_index] = min(min_distances[dist_index], distance_list[dist_index])
    adjacency_matrix = [[999 for _ in range(distance_count)] for _ in range(distance_count)]
    for row_index in range(distance_count - 1):
        row_values = [int(value) for value in input().split()]
        for col_offset in range(distance_count - 1 - row_index):
            if row_values[col_offset] != 0:
                adjacency_matrix[row_index][col_offset + row_index + 1] = row_values[col_offset]
                adjacency_matrix[col_offset + row_index + 1][row_index] = row_values[col_offset]
    unvisited_flags = [1 for _ in range(distance_count)]
    total_distance = 0
    for _ in range(distance_count):
        min_index = min_distances.index(min(min_distances))
        total_distance += min_distances[min_index]
        unvisited_flags[min_index] = 0
        min_distances[min_index] = 999
        for neighbor_index in range(distance_count):
            if unvisited_flags[neighbor_index]:
                min_distances[neighbor_index] = min(min_distances[neighbor_index], adjacency_matrix[min_index][neighbor_index])
    print(total_distance)