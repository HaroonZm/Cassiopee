import sys
readline = sys.stdin.readline
write = sys.stdout.write

while True:
    line = readline()
    if not line:
        break
    N = int(line)
    if N == 0:
        break
    P = []
    for _ in range(N):
        P.append(list(map(float, readline().split())))
    CS = []
    R = [-1]*N
    for i in range(N):
        pxi, pyi, pzi, vxi, vyi, vzi, ri, vri = P[i]
        R[i] = ri / vri
    for i in range(N):
        pxi, pyi, pzi, vxi, vyi, vzi, ri, vri = P[i]
        for j in range(i+1, N):
            pxj, pyj, pzj, vxj, vyj, vzj, rj, vrj = P[j]
            X0 = pxi - pxj
            X1 = vxi - vxj
            Y0 = pyi - pyj
            Y1 = vyi - vyj
            Z0 = pzi - pzj
            Z1 = vzi - vzj
            R0 = ri + rj
            R1 = - vri - vrj
            A = X1**2 + Y1**2 + Z1**2 - R1**2
            B = 2*X0*X1 + 2*Y0*Y1 + 2*Z0*Z1 - 2*R0*R1
            C = X0**2 + Y0**2 + Z0**2 - R0**2
            D = B**2 - 4*A*C
            if D < 0:
                continue
            DS = D**0.5
            if -B - DS > 0:
                t = (-B - DS) / (2*A)
                if t < R[i] and t < R[j]:
                    CS.append((t, i, j))
    CS.sort()
    U = [0]*N
    for c in CS:
        t, a, b = c
        if U[a] or U[b]:
            continue
        U[a] = 1
        U[b] = 1
        R[a] = t
        R[b] = t
    for i in range(N):
        write("%.16f\n" % R[i])