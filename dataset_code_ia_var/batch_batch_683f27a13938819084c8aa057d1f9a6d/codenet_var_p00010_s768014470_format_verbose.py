from math import acos
from math import sin

def compute_angle_between_vectors(
    point1_x, point1_y,
    origin_x, origin_y,
    point2_x, point2_y
):
    vector1_x = point1_x - origin_x
    vector1_y = point1_y - origin_y
    vector2_x = point2_x - origin_x
    vector2_y = point2_y - origin_y

    vector1_length_squared = vector1_x ** 2 + vector1_y ** 2
    vector2_length_squared = vector2_x ** 2 + vector2_y ** 2

    dot_product = vector1_x * vector2_x + vector1_y * vector2_y
    denominator = (vector1_length_squared * vector2_length_squared) ** 0.5

    angle_radians = acos(dot_product / denominator)
    return angle_radians

def compute_circumcircle_of_triangle(
    vertex1_x, vertex1_y,
    vertex2_x, vertex2_y,
    vertex3_x, vertex3_y
):
    double_angle_at_vertexA = sin(2 * compute_angle_between_vectors(
        vertex3_x, vertex3_y,
        vertex1_x, vertex1_y,
        vertex2_x, vertex2_y
    ))

    double_angle_at_vertexB = sin(2 * compute_angle_between_vectors(
        vertex1_x, vertex1_y,
        vertex2_x, vertex2_y,
        vertex3_x, vertex3_y
    ))

    double_angle_at_vertexC = sin(2 * compute_angle_between_vectors(
        vertex2_x, vertex2_y,
        vertex3_x, vertex3_y,
        vertex1_x, vertex1_y
    ))

    sum_of_double_angles = (
        double_angle_at_vertexA +
        double_angle_at_vertexB +
        double_angle_at_vertexC
    )

    circumcenter_x = (
        double_angle_at_vertexA * vertex1_x +
        double_angle_at_vertexB * vertex2_x +
        double_angle_at_vertexC * vertex3_x
    ) / sum_of_double_angles + 0.0

    circumcenter_y = (
        double_angle_at_vertexA * vertex1_y +
        double_angle_at_vertexB * vertex2_y +
        double_angle_at_vertexC * vertex3_y
    ) / sum_of_double_angles + 0.0

    edge_length_between_vertex2_and_vertex3 = (
        (vertex2_x - vertex3_x) ** 2 +
        (vertex2_y - vertex3_y) ** 2
    ) ** 0.5

    angle_opposite_vertex1 = compute_angle_between_vectors(
        vertex2_x, vertex2_y,
        vertex1_x, vertex1_y,
        vertex3_x, vertex3_y
    )

    circumcircle_radius = (
        edge_length_between_vertex2_and_vertex3 /
        (2 * sin(angle_opposite_vertex1))
    ) + 0.0

    return circumcenter_x, circumcenter_y, circumcircle_radius

number_of_test_cases = int(input())

for test_case_index in range(number_of_test_cases):
    triangle_coordinates = tuple(map(float, input().split()))
    circumcircle_parameters = compute_circumcircle_of_triangle(*triangle_coordinates)
    print(
        "{0[0]:.3f} {0[1]:.3f} {0[2]:.3f}".format(circumcircle_parameters)
    )