import sys
readline = sys.stdin.readline
write = sys.stdout.write

MOD = 10**9 + 7

N, Q = map(int, readline().split())
P = list(map(int, readline().split()))
S = [0]*N
K = [0]*N
used = [0]*N

i = 0
while i < N:
    if used[i]:
        i += 1
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
    for x in vs:
        S[x] = s
        K[x] = l % MOD
    i += 1

def simple_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

N0 = 1
while N0 < N:
    N0 <<= 1
S0 = [0]*(2*N0)
K0 = [1]*(2*N0)
for i in range(N):
    S0[N0-1+i] = S[i]
    K0[N0-1+i] = K[i]

i = N0-2
while i >= 0:
    k0 = K0[2*i+1]
    k1 = K0[2*i+2]
    s0 = S0[2*i+1]
    s1 = S0[2*i+2]
    g = simple_gcd(k0, k1)
    newk = k0 // g * k1
    news = ((s0*k1 + s1*k0) // g) % MOD
    K0[i] = newk
    S0[i] = news
    i -= 1

for _ in range(Q):
    l, r = map(int, readline().split())
    L = l - 1 + N0
    R = r + N0
    k = 1
    s = 0
    while L < R:
        if R & 1:
            R -= 1
            kg, sg = K0[R-1], S0[R-1]
            g = simple_gcd(k, kg)
            newk = k // g * kg
            s = ((s*kg + sg*k) // g) % MOD
            k = newk
        if L & 1:
            kg, sg = K0[L-1], S0[L-1]
            g = simple_gcd(k, kg)
            newk = k // g * kg
            s = ((s*kg + sg*k) // g) % MOD
            k = newk
            L += 1
        L >>= 1; R >>= 1
    write("%d\n" % s)