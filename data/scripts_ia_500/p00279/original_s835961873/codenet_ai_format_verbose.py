import sys
import operator
import math

def calculate_triangle_area(point_a, point_b, point_c):
    return calculate_cross_product(point_b - point_a, point_c - point_a) / 2

def calculate_cosine_of_angle(vector_a, vector_b):
    return calculate_dot_product(vector_a, vector_b) / (abs(vector_a) * abs(vector_b))

def calculate_dot_product(vector_a, vector_b):
    return vector_a.real * vector_b.real + vector_a.imag * vector_b.imag

def calculate_cross_product(vector_a, vector_b):
    return vector_a.real * vector_b.imag - vector_a.imag * vector_b.real

def solve_minimum_area_polygon(current_point, other_points):
    sorted_points_by_angle = sorted(other_points, key=lambda point: (point.real - current_point.real) / abs(point - current_point), reverse=True)

    max_polygon_size = max(query_sizes) + 1

    area_minimum = [
        [
            [(float('inf'),) for _ in range(len(sorted_points_by_angle))]
            for _ in range(len(sorted_points_by_angle))
        ]
        for _ in range(max_polygon_size)
    ]

    # Initialize area for triangles
    for left_index in range(len(sorted_points_by_angle) - 1):
        for right_index in range(left_index + 1, len(sorted_points_by_angle)):
            area_minimum[3][left_index][right_index] = (
                calculate_triangle_area(current_point, sorted_points_by_angle[left_index], sorted_points_by_angle[right_index]),
                (current_point, sorted_points_by_angle[left_index], sorted_points_by_angle[right_index])
            )

    # Calculate areas for polygons of size 4 to max_polygon_size - 1
    for polygon_size in range(4, max_polygon_size):
        for left_index in range(len(sorted_points_by_angle)):
            for middle_index in range(left_index + 1, len(sorted_points_by_angle)):
                for right_index in range(middle_index + 1, len(sorted_points_by_angle)):
                    if math.isinf(area_minimum[polygon_size - 1][left_index][middle_index][0]):
                        continue

                    if calculate_triangle_area(sorted_points_by_angle[left_index], sorted_points_by_angle[middle_index], sorted_points_by_angle[right_index]) <= 0:
                        continue  # Skip if polygon is not convex

                    combined_area = area_minimum[3][middle_index][right_index][0] + area_minimum[polygon_size - 1][left_index][middle_index][0]
                    
                    if not math.isnan(area_minimum[polygon_size][middle_index][right_index][0]) and area_minimum[polygon_size][middle_index][right_index][0] < combined_area:
                        continue

                    area_minimum[polygon_size][middle_index][right_index] = (
                        combined_area,
                        area_minimum[polygon_size - 1][left_index][middle_index][1] + (sorted_points_by_angle[right_index],)
                    )
    
    minimal_polygons_areas = [(float('inf'),)] * max_polygon_size
    for polygon_size in range(3, max_polygon_size):
        minimal_polygons_areas[polygon_size] = min(
            [polygon_candidate for polygon_list in area_minimum[polygon_size] for polygon_candidate in polygon_list],
            key=operator.itemgetter(0)
        )
    
    return minimal_polygons_areas


input_file = sys.stdin

coordinate_count = int(input_file.readline())
coordinates = [
    [int(value) for value in input_file.readline().split()]
    for _ in range(coordinate_count)
]

query_count = int(input_file.readline())
query_sizes = [int(input_file.readline()) for _ in range(query_count)]

complex_points = [x + y * 1j for x, y in coordinates]
point_id_mapping = {point: index + 1 for index, point in enumerate(complex_points)}

complex_points.sort(key=operator.attrgetter('imag', 'real'))

minimum_area_per_polygon_size = [(float('inf'),) for _ in range(max(query_sizes) + 1)]

while len(complex_points) > 2:
    current_reference_point = complex_points.pop(0)
    solutions_for_current_reference = solve_minimum_area_polygon(current_reference_point, complex_points)
    minimum_area_per_polygon_size = [
        min(previous_minimum, current_solution, key=operator.itemgetter(0))
        for previous_minimum, current_solution in zip(minimum_area_per_polygon_size, solutions_for_current_reference)
    ]

for polygon_size_query in query_sizes:
    if math.isinf(minimum_area_per_polygon_size[polygon_size_query][0]):
        print('NA')
    else:
        print(*[point_id_mapping[point] for point in minimum_area_per_polygon_size[polygon_size_query][1]])