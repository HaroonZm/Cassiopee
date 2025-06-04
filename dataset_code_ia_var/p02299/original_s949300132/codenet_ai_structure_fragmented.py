def read_integer():
    return int(input())

def read_integers():
    return list(map(int, input().split()))

def read_polygon_vertex():
    return read_integers()

def read_polygon(n):
    return [read_polygon_vertex() for _ in range(n)]

def read_query():
    return read_integers()

def read_queries(q):
    return [read_query() for _ in range(q)]

def create_vector(a, b):
    return [a[0] - b[0], a[1] - b[1]]

def vector_dot_product(a, b):
    return sum([i * j for i, j in zip(a, b)])

def vector_cross_product(a, b):
    return a[0] * b[1] - a[1] * b[0]

def absolute_value(x):
    return abs(x)

def compare_with_epsilon(x, eps):
    return absolute_value(x) < eps

def is_inside_x(a_y, b_y, EPS):
    return a_y < EPS and EPS < b_y

def is_point_on_segment(a, b, EPS):
    return compare_with_epsilon(vector_cross_product(a, b), EPS) and vector_dot_product(a, b) < EPS

def update_x(x):
    return not x

def get_next_index(i, n):
    return (i + 1) % n

def polygon_contains_point(g, p, n, EPS):
    x = False
    for i in range(n):
        a = create_vector(g[i], p)
        b = create_vector(g[get_next_index(i, n)], p)
        if is_point_on_segment(a, b, EPS):
            return 1
        if a[1] > b[1]:
            a, b = b, a
        if is_inside_x(a[1], b[1], EPS) and vector_cross_product(a, b) > EPS:
            x = update_x(x)
    return 2 if x else 0

def process_queries(g, n, q, queries, EPS):
    for xy in queries:
        x, y = xy
        print(polygon_contains_point(g, [x, y], n, EPS))

def main():
    EPS = 0.001
    n = read_integer()
    g = read_polygon(n)
    q = read_integer()
    queries = [read_query() for _ in range(q)]
    process_queries(g, n, q, queries, EPS)

main()