number_of_polygon_vertices = int(input())

polygon_vertices = []

polygon_area_sum = 0

for vertex_index in range(number_of_polygon_vertices):
    vertex_coordinates = [int(coordinate) for coordinate in input().split()]
    polygon_vertices.append(vertex_coordinates)

polygon_vertices.append(polygon_vertices[0])

for vertex_index in range(number_of_polygon_vertices):
    x_current = polygon_vertices[vertex_index][0]
    y_current = polygon_vertices[vertex_index][1]
    x_next = polygon_vertices[vertex_index + 1][0]
    y_next = polygon_vertices[vertex_index + 1][1]
    polygon_area_sum += x_current * y_next - y_current * x_next

polygon_area = polygon_area_sum * 0.5

print(polygon_area)