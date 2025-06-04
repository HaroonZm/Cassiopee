import sys
readline = sys.stdin.readline
write = sys.stdout.write
while True:
    N_line = readline()
    if not N_line:
        break
    N = int(N_line)
    if N == 0:
        break
    C = []
    for i in range(N):
        C.append(list(map(int, readline().split())))
    e = 2**.5/2
    r_min = max(r*e for x, r in C)
    r_max = max(r for x, r in C)
    H = []
    for i in range(N-1):
        x0, r0 = C[i]
        x1, r1 = C[i+1]
        dx = x1 - x0
        l = (r0**2 + dx**2 - r1**2) / (2*dx)
        h = (r0**2 - l**2)**.5
        H.append(h)
    left = r_min
    right = r_max+1
    EPS = 1e-5
    while right - left > EPS:
        mid = (left + right) / 2
        h = mid
        k = -1
        found = False
        i = 0
        while i < N:
            xi, ri = C[i]
            if k == -1:
                if h <= ri:
                    k = i
            else:
                if i-1 < len(H) and H[i-1] < h:
                    if k != -1:
                        xp, rp = C[k]
                        xq, rq = C[i-1]
                        x0 = xp - (rp**2 - h**2)**.5
                        x1 = xq + (rq**2 - h**2)**.5
                        if x1 - x0 >= 2*h:
                            found = True
                            break
                    if h <= ri:
                        k = i
                    else:
                        k = -1
            i += 1
        if not found:
            if k == -1:
                check_result = False
            else:
                xp, rp = C[k]
                xq, rq = C[N-1]
                x0 = xp - (rp**2 - h**2)**.5
                x1 = xq + (rq**2 - h**2)**.5
                check_result = x1 - x0 >= 2*h
        else:
            check_result = True
        if check_result:
            left = mid
        else:
            right = mid
    write("%.16f\n" % (left*2))