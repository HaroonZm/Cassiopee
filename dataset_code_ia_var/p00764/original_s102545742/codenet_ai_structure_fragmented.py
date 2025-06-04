from math import sqrt
from sys import stdin, stdout

def get_readline():
    return stdin.readline

def get_write():
    return stdout.write

def input_n(readline):
    return int(readline())

def input_circle(readline, n):
    circles = []
    for _ in range(n):
        circles.append(list(map(int, readline().split())))
    return circles

def set_initial_points(C, n):
    P = {}
    P[(0, 0)] = tuple(C[0][:2])
    P[(n, 0)] = tuple(C[-1][:2])
    return P

def get_ex_ey(x0, y0, x1, y1, rd):
    ex = (x1 - x0) / rd
    ey = (y1 - y0) / rd
    return ex, ey

def get_rd(x0, y0, x1, y1):
    rr = (x1 - x0)**2 + (y1 - y0)**2
    rd = sqrt(rr)
    return rr, rd

def get_rc_rs(r0, rr, r1, rd):
    rc = (r0**2 + rr - r1**2) / (2 * rd)
    temp = 4 * r0**2 * rr - (r0**2 + rr - r1**2) ** 2
    rs = sqrt(temp) / (2 * rd) if temp > 0 else 0.0
    return rc, rs

def get_bx_by(x0, y0, ex, ey, rc):
    bx = x0 + ex * rc
    by = y0 + ey * rc
    return bx, by

def calculate_intersections(n, C):
    P = set_initial_points(C, n)
    for i in range(n - 1):
        x0, y0, r0 = C[i]
        x1, y1, r1 = C[i + 1]
        rr, rd = get_rd(x0, y0, x1, y1)
        rc, rs = get_rc_rs(r0, rr, r1, rd)
        ex, ey = get_ex_ey(x0, y0, x1, y1, rd)
        bx, by = get_bx_by(x0, y0, ex, ey, rc)
        P[(i + 1, 0)] = (bx + ey * rs, by - ex * rs)
        P[(i + 1, 1)] = (bx - ey * rs, by + ex * rs)
    return P

def calc(p0, p1):
    x0, y0 = p0
    x1, y1 = p1
    return sqrt((x1 - x0)**2 + (y1 - y0)**2)

def cross(a, b, c):
    x0, y0 = a
    x1, y1 = b
    x2, y2 = c
    return (x1 - x0) * (y2 - y0) - (x2 - x0) * (y1 - y0)

def propagate_for_point(i, j, n, P, dist, INF, gp):
    pos = P[(i, j)]
    d = dist[(i, j)]
    left = right = p_left = p_right = None
    for k in range(i + 1, n):
        lp = P[(k, 0)]
        rp = P[(k, 1)]
        if left is None or cross(pos, left, lp) >= 0:
            left = lp
        if right is None or cross(pos, rp, right) >= 0:
            right = rp
        if cross(pos, left, right) < 0:
            break
        if p_left != left:
            dist[(k, 0)] = min(dist.get((k, 0), INF), d + calc(pos, left))
            p_left = left
        if p_right != right:
            dist[(k, 1)] = min(dist.get((k, 1), INF), d + calc(pos, right))
            p_right = right
    else:
        send_to_goal(pos, left, right, gp, d, dist, n, INF)

def send_to_goal(pos, left, right, gp, d, dist, n, INF):
    if (left is None and right is None) or (cross(pos, left, gp) >= 0 and cross(pos, gp, right) >= 0):
        dist[(n, 0)] = min(dist.get((n, 0), INF), d + calc(pos, gp))

def dijkstra_like(P, n):
    INF = 10 ** 18
    dist = { (0,0): 0 }
    gp = P[(n, 0)]
    for i, j in sorted(P):
        propagate_for_point(i, j, n, P, dist, INF, gp)
    return dist

def process_case(n, readline, write):
    C = input_circle(readline, n)
    P = calculate_intersections(n, C)
    dist = dijkstra_like(P, n)
    write("%.06f\n" % dist[(n, 0)])

def main_loop():
    readline = get_readline()
    write = get_write()
    while True:
        n = input_n(readline)
        if n == 0:
            break
        process_case(n, readline, write)

main_loop()