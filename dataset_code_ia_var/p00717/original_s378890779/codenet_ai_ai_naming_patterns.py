def are_polygons_equivalent(poly_a, poly_b):
    for rotation_index in range(4):
        for reflect_index in range(4):
            if poly_a == poly_b:
                return True
            poly_b = [[y, -x] for x, y in poly_b]
        poly_b = [[x - poly_b[-1][0], y - poly_b[-1][1]] for x, y in poly_b][::-1]
    return False

while True:
    polygon_count = int(raw_input())
    if polygon_count == 0:
        break
    polygons = []
    for polygon_index in xrange(polygon_count + 1):
        vertex_count = int(raw_input())
        vertices = [map(int, raw_input().split()) for _ in xrange(vertex_count)]
        normalized_vertices = [[x - vertices[0][0], y - vertices[0][1]] for x, y in vertices]
        polygons.append(normalized_vertices)
    for comparison_index in xrange(1, polygon_count + 1):
        if are_polygons_equivalent(polygons[0], polygons[comparison_index]):
            print comparison_index
    print "+++++"