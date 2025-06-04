import sys

def read_line():
    return sys.stdin.readline()

def write_output(s):
    sys.stdout.write(s)

def dot_product3(p0, p1, p2):
    x0, y0 = p0
    x1, y1 = p1
    x2, y2 = p2
    return (x1 - x0) * (x2 - x0) + (y1 - y0) * (y2 - y0)

def cross_product3(p0, p1, p2):
    x0, y0 = p0
    x1, y1 = p1
    x2, y2 = p2
    return (x1 - x0) * (y2 - y0) - (y1 - y0) * (x2 - x0)

def distance2(p0, p1):
    x0, y0 = p0
    x1, y1 = p1
    return (x0 - x1)**2 + (y0 - y1)**2

def solve():
    N = int(read_line())
    P = []
    for i in range(N):
        nums = list(map(int, read_line().split()))
        P.append(nums)
    ok = 1
    for i in range(N - 1):
        p0 = P[i]
        p1 = P[i + 1]
        d0 = distance2(p0, p1) ** 0.5
        el0 = [-d0, d0]
        el1 = [-d0, d0]
        er0 = [-d0, d0]
        er1 = [-d0, d0]
        for j in range(i):
            q0 = P[j]
            d1 = distance2(p0, q0) ** 0.5
            d2 = distance2(p1, q0) ** 0.5
            sv = cross_product3(p0, p1, q0)
            cv0 = dot_product3(p0, p1, q0) / d1
            cv1 = dot_product3(p1, p0, q0) / d2
            if sv > 0:
                if cv0 > el0[0]:
                    el0[0] = cv0
                if -cv1 > el1[0]:
                    el1[0] = -cv1
            else:
                if -cv0 < er0[1]:
                    er0[1] = -cv0
                if cv1 < er1[1]:
                    er1[1] = cv1
        for j in range(i+2, N):
            q1 = P[j]
            d1 = distance2(p1, q1) ** 0.5
            d2 = distance2(p0, q1) ** 0.5
            sv = cross_product3(p1, p0, q1)
            cv0 = dot_product3(p1, p0, q1) / d1
            cv1 = dot_product3(p0, p1, q1) / d2
            if sv > 0:
                if cv0 > er1[0]:
                    er1[0] = cv0
                if -cv1 > er0[0]:
                    er0[0] = -cv1
            else:
                if -cv0 < el1[1]:
                    el1[1] = -cv0
                if cv1 < el0[1]:
                    el0[1] = cv1
        if not (max(el0[0], er0[0]) <= min(el0[1], er0[1])) or not (max(el1[0], er0[0]) <= min(el1[1], er1[1])):
            ok = 0
            break
    if ok:
        write_output("Possible\n")
    else:
        write_output("Impossible\n")

solve()