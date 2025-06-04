import sys
from math import sqrt, hypot

def compute_distance(point_a, point_b):
    return hypot(point_b[0] - point_a[0], point_b[1] - point_a[1])

def compute_triangle_area(vertex_a, vertex_b, vertex_c):
    side_ab = compute_distance(vertex_a, vertex_b)
    side_bc = compute_distance(vertex_b, vertex_c)
    side_ca = compute_distance(vertex_c, vertex_a)
    semi_perimeter = (side_ab + side_bc + side_ca) / 2
    return sqrt(semi_perimeter * (semi_perimeter - side_ab) * (semi_perimeter - side_bc) * (semi_perimeter - side_ca))

input_points_list = [tuple(map(float, input_line.split(","))) for input_line in sys.stdin]
total_area = 0.0
for current_vertex, next_vertex in zip(input_points_list[1:], input_points_list[2:]):
    total_area += compute_triangle_area(input_points_list[0], current_vertex, next_vertex)
print(total_area)