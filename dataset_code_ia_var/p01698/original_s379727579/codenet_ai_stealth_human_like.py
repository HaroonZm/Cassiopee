import sys
readline = sys.stdin.readline
write = sys.stdout.write

def solve():
    N = int(readline())
    if N == 0:  # Just check if we’re done
        return False
    # gather input
    P = []
    for x in range(N):
        row = readline().split()
        # let's just map everything straight to float, seems ok
        P.append(list(map(float, row)))
    CS = []
    R = [-1 for _ in range(N)]
    for idx in range(N):  # Calculate initial times
        pxi, pyi, pzi, vxi, vyi, vzi, ri, vri = P[idx]
        if vri != 0:
            R[idx] = ri / vri
        else:
            R[idx] = float('inf')  # ok, avoiding division by zero
    # pairwise intersections
    for i in range(N):
        pxi, pyi, pzi, vxi, vyi, vzi, ri, vri = P[i]
        for j in range(i+1, N):
            pxj, pyj, pzj, vxj, vyj, vzj, rj, vrj = P[j]
            # relative positions and velocities & radius stuff
            X0 = pxi - pxj
            X1 = vxi - vxj
            Y0 = pyi - pyj
            Y1 = vyi - vyj
            Z0 = pzi - pzj
            Z1 = vzi - vzj
            R0 = ri + rj
            R1 = -vri - vrj
            # quadratic formula time (classic)
            A = X1*X1 + Y1*Y1 + Z1*Z1 - R1*R1
            B = 2*X0*X1 + 2*Y0*Y1 + 2*Z0*Z1 - 2*R0*R1
            C = X0*X0 + Y0*Y0 + Z0*Z0 - R0*R0
            D = B*B - 4*A*C
            if D < 0:
                # no real solution, these guys never meet
                continue
            DS = D ** 0.5
            if (-B - DS) > 0:  # only care about positive t (future)
                t = (-B - DS) / (2*A)
                # can't be after either's timeout
                if t < R[i] and t < R[j]:
                    CS.append((t, i, j))
    # now take care of all collisions
    CS.sort()
    U = [0]*N  # already collided
    for incident in CS:
        t, a, b = incident
        if U[a] or U[b]:
            continue
        U[a] = U[b] = 1
        R[a] = R[b] = t
    # print result
    for r in R:
        # using 16 decimals, probably more than enough
        write("%.16f\n" % r)
    return True

while solve():
    pass  # my favorite placeholder, works fine here