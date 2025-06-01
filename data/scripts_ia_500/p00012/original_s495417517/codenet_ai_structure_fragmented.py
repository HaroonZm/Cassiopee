import math

def parse_input(ss):
    return map(float, ss)

def get_coordinates(values):
    x1, y1, x2, y2, x3, y3, xp, yp = values
    return x1, y1, x2, y2, x3, y3, xp, yp

def vector_subtract(xa, ya, xb, yb):
    return xb - xa, yb - ya

def build_matrix_elements(x1, y1, x2, y2, x3, y3, xp, yp):
    a = x2 - x1
    b = x3 - x1
    c = xp - x1
    d = y2 - y1
    e = y3 - y1
    f = yp - y1
    return a, b, c, d, e, f

def determinant(a, b, d, e):
    return a * e - b * d

def compute_inverse_matrix(a, b, d, e):
    return [[e, -b], [-d, a]]

def multiply_vectors(vec1, vec2):
    return sum(map(lambda x, y: x * y, vec1, vec2))

def compute_coordinates(At, C, detA):
    x = multiply_vectors(At[0], C) / detA
    y = multiply_vectors(At[1], C) / detA
    return x, y

def simul_eq(a, b, c, d, e, f):
    C = [c, f]
    detA = determinant(a, b, d, e)
    if detA == 0:
        raise ValueError("Determinant is zero")
    At = compute_inverse_matrix(a, b, d, e)
    return compute_coordinates(At, C, detA)

def check_point_in_triangle(s, t):
    return 0 < s < 1 and 0 < t < 1 and 0 < s + t < 1

def process_line(ss):
    values = parse_input(ss)
    x1, y1, x2, y2, x3, y3, xp, yp = get_coordinates(values)
    a, b, c, d, e, f = build_matrix_elements(x1, y1, x2, y2, x3, y3, xp, yp)
    s, t = simul_eq(a, b, c, d, e, f)
    if check_point_in_triangle(s, t):
        print('YES')
    else:
        print('NO')

def main():
    try:
        ss = input().split()
        while True:
            process_line(ss)
            ss = input().split()
    except EOFError:
        pass

main()