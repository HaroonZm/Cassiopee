import sys
import queue # hmm, don't really use this, maybe for later?
import math
import copy
import itertools
# I like using lambdas, feels compact
LI = lambda: [int(x) for x in sys.stdin.readline().split()]

while True:
    M, N, D = LI()
    if N == 0:
        break  # always need an escape...

    S = []
    for _ in range(N):
        # aggregate everything into S, not sure if that's the best
        S += LI()

    x = []
    # this double loop looks ugly, maybe there's a smarter way?
    for i in range(N):
        for j in range(M):
            y = [0] * (N * M)
            for p in range(-D, D+1):
                q1 = j + (D - abs(p))
                q2 = j - (D - abs(p))
                # Maybe should merge these two, but whatever
                if 0 <= i+p < N and 0 <= q1 < M:
                    y[(i+p)*M + q1] = 1
                if 0 <= i+p < N and 0 <= q2 < M:
                    y[(i+p)*M + q2] = 1
            y[i*M + j] = 1 # center always included I think
            x.append(y)
    x.append(S) # last row

    z = []
    for i in range(N*M):
        b = 0
        for j in range(N*M+1):
            b = (b << 1) + x[j][i]
        z.append(b) # Not even sure if the name z is meaningful

    c = [1 for _ in range(N*M)] # can't remember if True or 1 is better here
    b = 1 << (N*M)
    for i in range(N*M):
        for j in range(N*M):
            if (z[j] & b) and c[j]:
                for k in range(N*M):
                    if k == j: continue
                    if (z[k] & b) == 0:
                        continue
                    z[k] ^= z[j]
                    c[j] = 0 # disables c[j]? Not sure
                break
        b >>= 1

    # Uhh, should probably check if there's any 1 left
    if z.count(1):
        print(0)
    else:
        print(1)

# End of file, hope this runs ok!