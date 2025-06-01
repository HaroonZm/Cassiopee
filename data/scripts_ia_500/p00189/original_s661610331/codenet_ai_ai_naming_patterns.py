NULL_VALUE = 10000
TOTAL_TOWNS = 10

while True:
    edge_count = int(input())

    if edge_count == 0:
        break

    distance_matrix = [[NULL_VALUE] * TOTAL_TOWNS for _ in range(TOTAL_TOWNS)]

    for town_index in range(TOTAL_TOWNS):
        distance_matrix[town_index][town_index] = 0

    max_town_index = 0

    for _ in range(edge_count):
        from_town, to_town, travel_time = map(int, input().split())

        distance_matrix[from_town][to_town] = travel_time
        distance_matrix[to_town][from_town] = travel_time

        max_town_index = max(max_town_index, from_town, to_town)

    for intermediate in range(max_town_index + 1):
        for start in range(max_town_index + 1):
            for end in range(max_town_index + 1):
                distance_matrix[start][end] = min(
                    distance_matrix[start][intermediate] + distance_matrix[intermediate][end],
                    distance_matrix[start][end]
                )

    minimum_total_time = NULL_VALUE
    central_town_index = -1

    for town_index, distances in enumerate(distance_matrix):
        reachable_distances = [distance for distance in distances if 0 < distance < NULL_VALUE]

        if reachable_distances:
            total_time = sum(reachable_distances)

            if total_time < minimum_total_time:
                minimum_total_time = total_time
                central_town_index = town_index

    print(central_town_index, minimum_total_time)