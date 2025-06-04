def read_input():
    import sys
    return sys.stdin

def parse_int(line):
    return int(line.strip())

def parse_complex_point(line):
    return string_to_complex(line)

def string_to_complex(s):
    x, y = map(int, s.split())
    return x + y * 1j

def get_polygon_points(file_input, n):
    points = []
    for _ in range(n):
        line = file_input.readline()
        point = parse_complex_point(line)
        points.append(point)
    return points

def close_polygon(points):
    points.append(points[0])
    return points

def get_queries(file_input, q):
    queries = []
    for _ in range(q):
        line = file_input.readline()
        t = parse_complex_point(line)
        queries.append(t)
    return queries

def process_remaining_lines(file_input):
    for line in file_input:
        yield parse_complex_point(line)

def dot_product(c1, c2):
    return c1.real * c2.real + c1.imag * c2.imag

def cross_product(c1, c2):
    return c1.real * c2.imag - c1.imag * c2.real

def swap_if_imag_greater(a, b):
    if a.imag > b.imag:
        return b, a
    return a, b

def is_point_on_edge(a, b):
    cross_ab = cross_product(a, b)
    if cross_ab == 0 and dot_product(a, b) <= 0:
        return True
    return False

def should_toggle_flag(a, b):
    cross_ab = cross_product(a, b)
    if a.imag <= 0 and b.imag > 0 and cross_ab > 0:
        return True
    return False

def point_location(polygon, point):
    flag = False
    for v1, v2 in zip(polygon[0:], polygon[1:]):
        a = v1 - point
        b = v2 - point
        a, b = swap_if_imag_greater(a, b)
        if is_point_on_edge(a, b):
            return 1
        if should_toggle_flag(a, b):
            flag = not flag
    return 2 if flag else 0

def process_query(polygon, point):
    return point_location(polygon, point)

def process_all_queries(polygon, file_input):
    for point in process_remaining_lines(file_input):
        res = process_query(polygon, point)
        print(res)

def main():
    file_input = read_input()
    n = parse_int(file_input.readline())
    polygon = get_polygon_points(file_input, n)
    polygon = close_polygon(polygon)
    q_line = file_input.readline()
    if q_line.strip().isdigit():
        q = parse_int(q_line)
        process_all_queries(polygon, file_input)
    else:
        process_all_queries(polygon, [q_line] + list(file_input))

main()