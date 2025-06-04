def compute_triangle_area_with_origin(vertex_vector_1, vertex_vector_2):
    
    return (
        vertex_vector_1.real * vertex_vector_2.imag
        - vertex_vector_1.imag * vertex_vector_2.real
    ) / 2

number_of_polygon_vertices = int(input())

polygon_vertices_as_complex = []

for input_index in range(number_of_polygon_vertices):
    
    vertex_x_coordinate, vertex_y_coordinate = map(int, input().split())
    
    vertex_as_complex_number = vertex_x_coordinate + vertex_y_coordinate * 1j
    
    polygon_vertices_as_complex.append(vertex_as_complex_number)

total_polygon_area = 0.0

for triangle_index in range(1, number_of_polygon_vertices - 1):
    
    vector_from_first_to_current = polygon_vertices_as_complex[triangle_index] - polygon_vertices_as_complex[0]
    
    vector_from_first_to_next = polygon_vertices_as_complex[triangle_index + 1] - polygon_vertices_as_complex[0]
    
    triangle_area = compute_triangle_area_with_origin(
        vector_from_first_to_current,
        vector_from_first_to_next
    )
    
    total_polygon_area += triangle_area

print("{:.1f}".format(total_polygon_area))