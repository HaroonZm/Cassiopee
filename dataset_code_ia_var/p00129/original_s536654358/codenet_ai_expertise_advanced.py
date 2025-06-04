import math
from functools import partial

def vector_length(v):
    return math.hypot(*v)

def input_vectors(n):
    return [list(map(int, input().split())) for _ in range(n)]

def cmp_fuzzy(a, b, eps=1e-6):
    return a > b or abs(a - b) < eps

def is_safe(entity, waypoints):
    tx, ty, sx, sy = entity
    vec_st = [tx - sx, ty - sy]
    rst = vector_length(vec_st)
    for wx, wy, r in waypoints:
        vec_wt = [tx - wx, ty - wy]
        vec_sw = [wx - sx, wy - sy]
        rwt = vector_length(vec_wt)
        rsw = vector_length(vec_sw)
        inside_t = rwt < r
        inside_s = rsw < r
        if rst == 0 or (inside_t and inside_s):
            continue
        if inside_t != inside_s:
            return False
        a = math.pi / 2 - math.acos(r / rsw)
        dot = vec_sw[0] * vec_st[0] + vec_sw[1] * vec_st[1]
        b = math.acos(max(-1, min(1, round(dot / (rsw * rst), 4))))
        if cmp_fuzzy(a, b) and cmp_fuzzy(rst ** 2, rsw ** 2 - r ** 2):
            return False
    return True

while True:
    try:
        n = int(input())
        if n == 0:
            break
        waypoints = input_vectors(n)
        for entity in input_vectors(int(input())):
            print("Safe" if is_safe(entity, waypoints) else "Danger")
    except EOFError:
        break