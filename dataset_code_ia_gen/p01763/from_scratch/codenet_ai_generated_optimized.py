import sys
input=sys.stdin.readline

N,M,D=map(int,input().split())
A=list(map(int,input().split()))
records=[list(map(int,input().split())) for _ in range(D)]

def crt(rems, mods):
    x, m = 0, 1
    for r_i, m_i in zip(rems, mods):
        if r_i == -1:
            continue
        r_i %= m_i
        # Solve x ≡ x (mod m), x ≡ r_i (mod m_i)
        # Extended Euclidean Algorithm
        g, p, q = ext_gcd(m, m_i)
        if (r_i - x) % g != 0:
            return None
        tmp = ((r_i - x) // g * p) % (m_i // g)
        x += m * tmp
        m *= m_i // g
        x %= m
    return x, m

def ext_gcd(a, b):
    if b==0:
        return a,1,0
    g,y,x=ext_gcd(b,a%b)
    y-= (a//b)*x
    return g,x,y

prev_set = set([N])
prev_max = N

for day in range(D):
    R = records[day]
    candidates = set()
    # Generate all x <= prev_max, x>=0, x <= N and satisfy residues R where known
    # Because residue on A_i is partial info, we find x with x mod lcm and residue
    # Among all x in [0, prev_max], we find x satisfying residues at R
    # We solve CRT to get base x0 and modulus M0
    res = crt(R,A)
    if res is None:
        print(-1)
        sys.exit()
    x0, M0 = res
    # We want x0 + k*M0 <= prev_max and x >=0
    # maximum x = x0 + floor((prev_max - x0)/M0)*M0 if >=0 else no solution
    if x0 > prev_max:
        print(-1)
        sys.exit()
    k = (prev_max - x0)//M0
    candidate = x0 + k*M0
    if candidate > prev_max or candidate < 0:
        print(-1)
        sys.exit()
    prev_max = candidate

print(prev_max)