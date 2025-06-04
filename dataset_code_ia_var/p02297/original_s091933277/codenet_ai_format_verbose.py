import math
import cmath

def calculate_triangle_area_from_origin(complex_point_start, complex_point_end):
    angle_start = cmath.phase(complex_point_start)
    rotated_vector = complex_point_end * complex(math.cos(-angle_start), math.sin(-angle_start))
    triangle_area = abs(complex_point_start) * rotated_vector.imag / 2
    return triangle_area

number_of_vertices = int(input())

polygon_vertices = []
for vertex_index in range(number_of_vertices):
    x_coordinate, y_coordinate = map(float, input().split())
    vertex_as_complex = complex(x_coordinate, y_coordinate)
    polygon_vertices.append(vertex_as_complex)

polygon_vertices.append(polygon_vertices[0])  # Close the polygon by repeating the first point

number_of_points_in_closed_polygon = len(polygon_vertices)

polygon_area_sum = 0.0
for start_index in range(number_of_points_in_closed_polygon - 1):
    start_vertex = polygon_vertices[start_index]
    end_vertex = polygon_vertices[start_index + 1]
    polygon_area_sum += calculate_triangle_area_from_origin(start_vertex, end_vertex)

print(round(polygon_area_sum, 1))