import sys
readline = sys.stdin.readline
write = sys.stdout.write

def gcd(m, n):
    while n:
        m, n = n, m % n
    return m

def solve():
    MOD = 10**9 + 7

    N, Q = map(int, readline().split())
    *P, = map(int, readline().split())
    S = [0]*N
    K = [0]*N
    used = [0]*N
    for i in range(N):
        if used[i]:
            continue
        vs = [i]
        s = i+1
        used[i] = 1
        v = P[i]-1
        while v != i:
            vs.append(v)
            s += v+1
            used[v] = 1
            v = P[v]-1
        l = len(vs)
        for v in vs:
            S[v] = s
            K[v] = l % MOD
    N0 = 2**(N-1).bit_length()
    S0 = [0]*(2*N0)
    K0 = [1]*(2*N0)
    for i in range(N):
        S0[N0-1+i] = S[i]
        K0[N0-1+i] = K[i]
    def calc(k0, k1, s0, s1):
        g = gcd(k0, k1)
        return k0 // g * k1, ((s0*k1 + s1*k0) // g) % MOD

    for i in range(N0-2, -1, -1):
        K0[i], S0[i] = calc(K0[2*i+1], K0[2*i+2], S0[2*i+1], S0[2*i+2])

    def query(l, r):
        L = l + N0; R = r + N0
        k = 1
        s = 0
        while L < R:
            if R & 1:
                R -= 1
                k, s = calc(k, K0[R-1], s, S0[R-1])

            if L & 1:
                k, s = calc(k, K0[L-1], s, S0[L-1])
                L += 1
            L >>= 1; R >>= 1
        return s

    for i in range(Q):
        l, r = map(int, readline().split())
        write("%d\n" % query(l-1, r))
solve()