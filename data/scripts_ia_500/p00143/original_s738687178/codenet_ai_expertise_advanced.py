from operator import sub
from sys import stdin

def cross(a, b):
    return a[0] * b[1] - a[1] * b[0]

def vector_subtract(a, b):
    return [x - y for x, y in zip(a, b)]

def all_positive_or_negative(iterable):
    s = set(x > 0 for x in iterable if x != 0)
    return len(s) == 1 and 0 not in iterable

input_lines = iter(stdin.read().splitlines())
for _ in range(int(next(input_lines))):
    line = list(map(int, next(input_lines).split()))
    points = list(zip(line[0:6:2], line[1:6:2]))
    edges = [vector_subtract(b, a) for a, b in zip(points, points[1:] + points[:1])]
    m_vectors = [vector_subtract(line[6:8], p) for p in points]
    f_vectors = [vector_subtract(line[8:10], p) for p in points]

    m_cross = [cross(m, e) for m, e in zip(m_vectors, edges)]
    f_cross = [cross(f, e) for f, e in zip(f_vectors, edges)]

    print("OK" if all_positive_or_negative(m_cross) != all_positive_or_negative(f_cross) else "NG")