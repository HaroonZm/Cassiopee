number_of_vertices = int(input())

range_of_vertices = range(number_of_vertices)

vertices_coordinates_list = []

for vertex_index in range_of_vertices:
    vertex_coordinates = [int(coordinate) for coordinate in input().split()]
    vertices_coordinates_list.append(vertex_coordinates)

signed_area_accumulator = 0

# Closing the polygon by repeating the first vertex at the end
vertices_coordinates_list.append(vertices_coordinates_list[0])

for current_vertex_index in range_of_vertices:
    current_vertex_x = vertices_coordinates_list[current_vertex_index][0]
    current_vertex_y = vertices_coordinates_list[current_vertex_index][1]
    next_vertex_x = vertices_coordinates_list[current_vertex_index + 1][0]
    next_vertex_y = vertices_coordinates_list[current_vertex_index + 1][1]

    signed_area_accumulator += (current_vertex_x * next_vertex_y) - (current_vertex_y * next_vertex_x)

polygon_area = 0.5 * abs(signed_area_accumulator)

print(polygon_area)