import sys

def read_input():
    n = int(raw_input())
    return n

def is_end(n):
    return n == 0

def read_points(n):
    points = []
    for _ in xrange(n):
        point = parse_point(raw_input())
        points.append(point)
    return points

def parse_point(line):
    return map(float, line.split(","))

def sort_points_by_y(points):
    return sorted(points, key=lambda x: x[1])

def subtract_points(a, b):
    return [a[0] - b[0], a[1] - b[1]]

def vector_length(v):
    return (v[0]**2 + v[1]**2) ** 0.5

def cosine_of_vector(v):
    length = vector_length(v)
    if length == 0:
        return 0
    return v[0] / length

def should_continue(point, p):
    return point[1] < p[1] or point == p

def compare_cosine(c, maxcos, direction):
    if direction == "r":
        return c >= maxcos
    elif direction == "l":
        return c <= maxcos
    return False

def update_maxcos(c, direction):
    return c

def next_point(d, p, maxcos, direction):
    q = None
    for i in xrange(1, len(d)):
        if should_continue(d[i], p):
            continue
        v = subtract_points(d[i], p)
        c = cosine_of_vector(v)
        if compare_cosine(c, maxcos[0], direction):
            maxcos[0] = update_maxcos(c, direction)
            q = d[i]
    return q

def add_to_hull(hull, q):
    hull.append(q)

def is_hull_end(q, d):
    return q == d[-1]

def calc_hull(d, direction):
    maxcos0 = {"r": -1.0, "l": 1.0}
    hull = [d[0]]
    p = d[0]
    while True:
        maxcos = [maxcos0[direction]]
        q = next_point(d, p, maxcos, direction)
        p = q
        add_to_hull(hull, q)
        if is_hull_end(q, d):
            break
    return hull

def compute_result(d):
    return len(d) - (len(calc_hull(d, "r") + calc_hull(d, "l")) - 2)

def main_loop():
    while True:
        n = read_input()
        if is_end(n):
            break
        d = read_points(n)
        d = sort_points_by_y(d)
        result = compute_result(d)
        print result

main_loop()