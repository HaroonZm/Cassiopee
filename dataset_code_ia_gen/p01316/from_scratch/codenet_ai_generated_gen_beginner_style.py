import sys

def clamp(value):
    if value < 0:
        return 0
    if value > 255:
        return 255
    return value

for line in sys.stdin:
    line=line.strip()
    if line=="0 0":
        break
    if line=="":
        continue
    N,M = map(int,line.split())
    codebook = []
    for _ in range(M):
        c = int(sys.stdin.readline())
        codebook.append(c)
    x = []
    for _ in range(N):
        xi = int(sys.stdin.readline())
        x.append(xi)

    # dp[i][y] = minimal sum of squared errors up to i-th sample with output y at position i
    # since y is between 0 and 255, for each position i we store a cost array of size 256
    # we also need previous values to reconstruct, but only minimal cost is required here
    # initial condition: y0=128, no cost for i=0 because no error at i=0 in problem?
    # careful, y0 corresponds to i=0, but input x has length N samples x[0..N-1]
    # from problem: y0=128 (initial)
    # and for i from 1 to N, y_i = y_{i-1} + C[k_i]
    # So, the sequence y has length N+1: y0..yN
    # x has length N: x0..xN-1
    # We want to minimize sum over i=0 to N-1 of (x_i - y_{i+1})^2
    # So dp over i in [0..N], dp[i][y] minimal cost up to i (amount of squared errors for the first i samples)
    # and y is the value of y_i
    # At i=0, y0=128 and cost=0

    INF = 10**15
    dp_prev = [INF]*256
    dp_prev[128] = 0

    for i in range(N):
        dp_curr = [INF]*256
        xi = x[i]
        for yprev in range(256):
            prev_cost = dp_prev[yprev]
            if prev_cost == INF:
                continue
            for c in codebook:
                ycur = clamp(yprev + c)
                diff = xi - ycur
                cost = prev_cost + diff*diff
                if cost < dp_curr[ycur]:
                    dp_curr[ycur] = cost
        dp_prev = dp_curr

    print(min(dp_prev))