from sys import exit
from functools import reduce
from math import gcd

def extgcd(a, b):
    # Extended Euclidean algorithm
    if b == 0:
        return a, 1, 0
    g, x, y = extgcd(b, a % b)
    return g, y, x - (a // b) * y

def crt(eq1, eq2):
    a1, m1 = eq1
    a2, m2 = eq2
    g = gcd(m1, m2)
    if (a1 - a2) % g:
        print(-1)
        exit()
    lcm = m1 // g * m2
    g2, p, q = extgcd(m1 // g, m2 // g)
    # Safe since m1//g and m2//g are coprime
    x = ((a2 * (m1 // g) * p) + (a1 * (m2 // g) * q)) % lcm
    return (x, lcm)

def build_eqs(P, Q, N):
    eqs = []
    for i in range(N):
        a = []
        x = i
        for j in range(3 * N):
            if P[x] == x:
                a.append(j)
                if len(a) == 2:
                    break
            x = Q[P[x]]
        if len(a) < 2:
            print(-1)
            exit()
        eqs.append((a[0], a[1] - a[0]))
    return eqs

def main():
    N = int(input())
    P = [p - 1 for p in map(int, input().split())]
    Q = [q - 1 for q in map(int, input().split())]

    eqs = build_eqs(P, Q, N)
    x, mod = reduce(crt, eqs, (0, 1))
    print(x % mod)

if __name__ == "__main__":
    main()