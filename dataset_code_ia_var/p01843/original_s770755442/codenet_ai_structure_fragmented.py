import sys

def get_readline():
    return sys.stdin.readline

def get_write():
    return sys.stdout.write

def cross3(p0, p1, q0):
    dx1 = p1[0] - p0[0]
    dy1 = p1[1] - p0[1]
    dx2 = q0[0] - p0[0]
    dy2 = q0[1] - p0[1]
    return dx1 * dy2 - dy1 * dx2

def unpack_points(p0, p1, q0, q1):
    x0, y0 = p0
    x1, y1 = p1
    x2, y2 = q0
    x3, y3 = q1
    return x0, y0, x1, y1, x2, y2, x3, y3

def compute_line_diffs(x0, y0, x1, y1, x2, y2, x3, y3):
    dx0 = x1 - x0
    dy0 = y1 - y0
    dx1 = x3 - x2
    dy1 = y3 - y2
    return dx0, dy0, dx1, dy1

def compute_s_and_sm(x0, y0, x2, y2, dx1, dy1, dx0, dy0):
    s = (y0 - y2) * dx1 - (x0 - x2) * dy1
    sm = dx0 * dy1 - dy0 * dx1
    return s, sm

def adjust_for_negative_sm(x0, y0, s, dx0, y0_val, dy0, sm):
    return -(x0 * sm + s * dx0), -(y0_val * sm + s * dy0), -sm

def adjust_for_positive_sm(x0, y0, s, dx0, y0_val, dy0, sm):
    return x0 * sm + s * dx0, y0_val * sm + s * dy0, sm

def cross_point(p0, p1, q0, q1):
    x0, y0, x1, y1, x2, y2, x3, y3 = unpack_points(p0, p1, q0, q1)
    dx0, dy0, dx1, dy1 = compute_line_diffs(x0, y0, x1, y1, x2, y2, x3, y3)
    s, sm = compute_s_and_sm(x0, y0, x2, y2, dx1, dy1, dx0, dy0)
    if sm < 0:
        return adjust_for_negative_sm(x0, y0, s, dx0, y0, dy0, sm)
    return adjust_for_positive_sm(x0, y0, s, dx0, y0, dy0, sm)

def input_N_M(readline):
    return map(int, readline().split())

def input_L(readline):
    return int(readline())

def input_PS(L, readline):
    return [list(map(int, readline().split())) for _ in range(L)]

def input_PSS(N, readline):
    return [input_PS(input_L(readline), readline) for _ in range(N)]

def input_QS(M, readline):
    return [list(map(int, readline().split())) for _ in range(M)]

def make_line_pairs(PSS, QS):
    LS = []
    for PS in PSS:
        for x0, y0 in PS:
            for x1, y1 in QS:
                LS.append(((x0, y0), (x1, y1)))
    return LS

def scale_point(x, y, r):
    return x*r, y*r

def scale_PS(PS, r):
    return [scale_point(x, y, r) for x, y in PS]

def scale_PSS(PSS, r):
    return [scale_PS(PS, r) for PS in PSS]

def scale_q_point(q, r):
    return q[0]*r, q[1]*r

def compute_C0(p0, q0, p1):
    return cross3(p0, q0, p1)

def compute_C1(p0, q0, q1):
    return cross3(p0, q0, q1)

def compute_D0(p1, q1, p0):
    return cross3(p1, q1, p0)

def compute_D1(p1, q1, q0):
    return cross3(p1, q1, q0)

def loop_edges(PS, l, p0, q0):
    for i in range(l):
        p1 = PS[i-1]
        q1 = PS[i]
        C0 = compute_C0(p0, q0, p1)
        C1 = compute_C1(p0, q0, q1)
        D0 = compute_D0(p1, q1, p0)
        D1 = compute_D1(p1, q1, q0)
        if C0 * C1 < 0 and D0 * D1 < 0:
            return True
    return False

def check(p, q, r, PSS, QS):
    p0 = (p, q)
    res = 0
    PSS1 = scale_PSS(PSS, r)
    for x1, y1 in QS:
        q0 = (x1 * r, y1 * r)
        for PS in PSS1:
            l = len(PS)
            if loop_edges(PS, l, p0, q0):
                break
        else:
            res += 1
    return res

def update_ans(ans, newval):
    return max(ans, newval)

def main():
    readline = get_readline()
    write = get_write()
    N, M = input_N_M(readline)
    PSS = input_PSS(N, readline)
    QS = input_QS(M, readline)
    LS = make_line_pairs(PSS, QS)
    ans = 0
    K = len(LS)
    for i in range(K):
        p0, p1 = LS[i]
        for j in range(i):
            q0, q1 = LS[j]
            p, q, r = cross_point(p0, p1, q0, q1)
            if r == 0:
                continue
            res = check(p, q, r, PSS, QS)
            ans = update_ans(ans, res)
    write("%d\n" % ans)

main()