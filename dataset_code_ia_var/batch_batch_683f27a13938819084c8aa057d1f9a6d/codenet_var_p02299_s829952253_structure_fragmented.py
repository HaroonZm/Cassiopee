def get_int():
    return int(input())

def get_complex():
    return complex(*map(int, input().split()))

def get_vertices(n):
    return [get_complex() for _ in range(n)]

def pair_vertices(vertices):
    return zip(vertices, vertices[1:] + [vertices[0]])

def to_edge_list(paired):
    return [(p0, p1) for p0, p1 in paired]

def input_vertices():
    n = get_int()
    vertices = get_vertices(n)
    edges = to_edge_list(pair_vertices(vertices))
    return edges

def read_points_query():
    return get_int()

def vector_sub(p0, p):
    return p0 - p

def get_vectors(p0, p1, p):
    return vector_sub(p0, p), vector_sub(p1, p)

def swap_if_needed(a, b):
    return (b, a) if a.imag > b.imag else (a, b)

def dot(a, b):
    return a.real * b.real + a.imag * b.imag

def cross(a, b):
    return a.real * b.imag - a.imag * b.real

def is_on_segment(a, b, crs):
    return crs == 0 and dot(a, b) <= 0

def is_crossing(a, b, crs):
    return a.imag <= 0 and 0 < b.imag and crs < 0

def count_crossings(edges, p):
    counter = 0
    for p0, p1 in edges:
        a, b = get_vectors(p0, p1, p)
        a, b = swap_if_needed(a, b)
        crs = cross(a, b)
        if is_crossing(a, b, crs):
            counter += 1
        if is_on_segment(a, b, crs):
            return 1
    return 2 if counter % 2 else 0

def handle_query(edges):
    p = get_complex()
    res = count_crossings(edges, p)
    print(res)

def main():
    edges = input_vertices()
    q = read_points_query()
    while q:
        q -= 1
        handle_query(edges)

main()