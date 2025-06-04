import sys
readline = sys.stdin.readline
write = sys.stdout.write

def solve():
    N, M = map(int, readline().split())
    A = list(map(int, readline().split()))
    P = list(map(int, readline().split()))
    def lcm(m, n):
        m0 = m
        n0 = n
        while n:
            m, n = n, m % n
        return m0 // m * n0
    N2 = 1 << N
    Q = [1] * N2
    L = [1] * N2
    C = [0] * N2
    for i in range(N):
        L[1 << i] = A[i]
        Q[1 << i] = P[i] / 100
    ans = 0
    for state in range(1, N2):
        b = state & -state
        L[state] = lcm(L[state ^ b], L[b])
        C[state] = C[state ^ b] + 1
        Q[state] = Q[state ^ b] * Q[b]
        if C[state] % 2:
            ans += Q[state] * (M // L[state])
        else:
            ans -= Q[state] * (M // L[state])
    write("%.16f\n" % ans)

solve()