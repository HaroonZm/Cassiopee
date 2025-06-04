import math as m

(a, b, c, d), g = list(map(int, input().split())), int(input())

Z = lambda u,v: c-a, d-b
p, q = Z(None, None)
L = m.sqrt(p*p + q*q)

pf = lambda e,f: ((e-a)*p + (f-b)*q)/(L*L)

for _ in range(g):
    s, t = [int(x) for x in input().split()]
    r = pf(s, t)
    print(a + r*p, b + r*q)