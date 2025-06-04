def read_vertex():
    return list(map(float, input().split(",")))
def calculate_triangle_area(vertex_a, vertex_b, vertex_c):
    return abs((vertex_a[0] - vertex_c[0]) * (vertex_b[1] - vertex_c[1]) - (vertex_a[1] - vertex_c[1]) * (vertex_b[0] - vertex_c[0])) / 2
polygon_base_vertex = read_vertex()
polygon_prev_vertex = read_vertex()
polygon_curr_vertex = read_vertex()
polygon_total_area = calculate_triangle_area(polygon_base_vertex, polygon_prev_vertex, polygon_curr_vertex)
while True:
    try:
        polygon_prev_vertex = polygon_curr_vertex
        polygon_curr_vertex = read_vertex()
        polygon_total_area += calculate_triangle_area(polygon_base_vertex, polygon_prev_vertex, polygon_curr_vertex)
    except:
        break
print(polygon_total_area)