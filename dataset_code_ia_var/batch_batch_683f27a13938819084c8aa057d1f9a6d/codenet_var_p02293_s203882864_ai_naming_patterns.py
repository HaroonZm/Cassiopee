EPSILON_TOLERANCE = 1e-4

def compute_outer_product(vector1, vector2):
    result = vector1.conjugate() * vector2
    return result.imag

def compute_inner_product(vector1, vector2):
    result = vector1.conjugate() * vector2
    return result.real

def determine_relationship(point_a, point_b, point_c, point_d):
    direction_vector1 = point_b - point_a
    direction_vector2 = point_d - point_c
    if abs(compute_outer_product(direction_vector1, direction_vector2)) <= EPSILON_TOLERANCE:
        return 2
    elif abs(compute_inner_product(direction_vector1, direction_vector2)) <= EPSILON_TOLERANCE:
        return 1
    else:
        return 0

number_of_queries = int(input())
for query_index in range(number_of_queries):
    input_coordinates = list(map(int, input().split()))
    points_list = [complex(input_coordinates[i], input_coordinates[i + 1]) for i in range(0, 8, 2)]
    result = determine_relationship(points_list[0], points_list[1], points_list[2], points_list[3])
    print(result)