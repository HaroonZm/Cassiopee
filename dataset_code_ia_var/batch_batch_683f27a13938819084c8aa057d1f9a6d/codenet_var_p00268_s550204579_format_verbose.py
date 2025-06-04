from math import atan2
from collections import defaultdict, deque

def compute_cross_product_for_three_points(point_a, point_b, point_c):
    return (
        (point_b[0] - point_a[0]) * (point_c[1] - point_a[1])
        - (point_b[1] - point_a[1]) * (point_c[0] - point_a[0])
    )

def compute_convex_hull_with_indices(points_with_indices):
    ordered_convex_hull = []
    total_points = len(points_with_indices)
    for point in points_with_indices:
        while (
            len(ordered_convex_hull) > 1 and
            compute_cross_product_for_three_points(
                ordered_convex_hull[-1],
                ordered_convex_hull[-2],
                point
            ) > 0
        ):
            ordered_convex_hull.pop()
        ordered_convex_hull.append(point)

    lower_hull_start_index = len(ordered_convex_hull)
    for index in range(total_points - 2, -1, -1):
        point = points_with_indices[index]
        while (
            len(ordered_convex_hull) > lower_hull_start_index and
            compute_cross_product_for_three_points(
                ordered_convex_hull[-1],
                ordered_convex_hull[-2],
                point
            ) > 0
        ):
            ordered_convex_hull.pop()
        ordered_convex_hull.append(point)
    return ordered_convex_hull

def is_sequence_contained_in_order(reference_sequence, test_sequence):
    current_reference_index = 0
    for element in test_sequence:
        if (
            current_reference_index < len(reference_sequence) and
            element == reference_sequence[current_reference_index]
        ):
            current_reference_index += 1
    return current_reference_index == len(reference_sequence)

while True:
    number_of_cities, number_of_roads = map(int, input().split())
    if number_of_cities == 0 and number_of_roads == 0:
        break

    road_neighbours_by_city = [[] for city_index in range(number_of_cities)]

    city_coordinates = [
        list(map(int, input().split())) for city_index in range(number_of_cities)
    ]
    city_coordinates_with_indices = [
        city_coordinates[city_index] + [city_index]
        for city_index in range(number_of_cities)
    ]
    city_coordinates_with_indices.sort()

    convex_hull_points = compute_convex_hull_with_indices(city_coordinates_with_indices)
    convex_hull_city_indices = list(map(lambda point: point[2], convex_hull_points))[:-1]
    first_city_on_hull_index = convex_hull_city_indices.index(
        min(convex_hull_city_indices)
    )
    convex_hull_city_indices = (
        convex_hull_city_indices[first_city_on_hull_index:]
        + convex_hull_city_indices[:first_city_on_hull_index]
    )

    for road_index in range(number_of_roads):
        source_city, destination_city = map(int, input().split())
        source_city -= 1
        destination_city -= 1
        road_neighbours_by_city[source_city].append(destination_city)
        road_neighbours_by_city[destination_city].append(source_city)

    for city_index in range(number_of_cities):
        base_x, base_y = city_coordinates[city_index]
        road_neighbours_by_city[city_index].sort(
            key=lambda neighbour_city_index: atan2(
                city_coordinates[neighbour_city_index][1] - base_y,
                city_coordinates[neighbour_city_index][0] - base_x
            )
        )

    polygon_identifier_by_edge = defaultdict(list)
    polygon_identifier = 0
    for starting_city_index in range(number_of_cities):
        for neighbour_edge_index, initial_neighbour_city_index in enumerate(
            road_neighbours_by_city[starting_city_index]
        ):
            previous_city = starting_city_index
            polygon_vertex_sequence = [starting_city_index]
            current_city = initial_neighbour_city_index
            edge_index_on_current_city = road_neighbours_by_city[
                current_city
            ].index(previous_city)
            while True:
                neighbours_of_current_city = road_neighbours_by_city[current_city]
                next_neighbour_index = (
                    (neighbours_of_current_city.index(previous_city) + 1)
                    % len(neighbours_of_current_city)
                )
                if current_city == starting_city_index and next_neighbour_index == neighbour_edge_index:
                    break
                polygon_vertex_sequence.append(current_city)
                previous_city, current_city = current_city, neighbours_of_current_city[next_neighbour_index]

            if (
                min(polygon_vertex_sequence) == starting_city_index and
                not is_sequence_contained_in_order(
                    convex_hull_city_indices,
                    polygon_vertex_sequence
                )
            ):
                for polygon_edge_index in range(len(polygon_vertex_sequence)):
                    point_a = polygon_vertex_sequence[polygon_edge_index - 1]
                    point_b = polygon_vertex_sequence[polygon_edge_index]
                    if not point_a < point_b:
                        point_a, point_b = point_b, point_a
                    polygon_identifier_by_edge[(point_a, point_b)].append(polygon_identifier)
                polygon_identifier += 1

    adjacency_by_polygon = [[] for polygon_index in range(polygon_identifier + 1)]

    for edge_to_polygons in polygon_identifier_by_edge.values():
        if len(edge_to_polygons) == 2:
            polygon_a, polygon_b = edge_to_polygons
        else:
            polygon_a = edge_to_polygons[0]
            polygon_b = polygon_identifier
        adjacency_by_polygon[polygon_a].append(polygon_b)
        adjacency_by_polygon[polygon_b].append(polygon_a)

    distances_from_outer_polygon = [-1] * (polygon_identifier + 1)
    outer_polygon_index = polygon_identifier
    distances_from_outer_polygon[outer_polygon_index] = 0
    bfs_queue = deque([outer_polygon_index])
    while bfs_queue:
        current_polygon = bfs_queue.popleft()
        current_distance = distances_from_outer_polygon[current_polygon]
        for adjacent_polygon in adjacency_by_polygon[current_polygon]:
            if distances_from_outer_polygon[adjacent_polygon] != -1:
                continue
            distances_from_outer_polygon[adjacent_polygon] = current_distance + 1
            bfs_queue.append(adjacent_polygon)

    print(max(distances_from_outer_polygon))