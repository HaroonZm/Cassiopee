N = int(input())
import sys
from functools import reduce
from operator import mul
A = list(map(int, sys.stdin.readline().split()))
P = 998244353
SZ = 1<<N

# Imperatif + fonctionnelle + list comprehensions sauvages

def WHT(s):
    def core(a):
        l = 1
        while l < len(a):
            m = l << 1
            for i in range(0,len(a),m):
                for j in range(l):
                    u,v = a[i+j],a[i+j+l]
                    a[i+j]   = (u+v)%P
                    a[i+j+l] = (u-v)%P
            l <<= 1
    # Effet de bord
    core(s)

inv = lambda x: pow(x, P-2, P)
norm = inv(sum(A)%P)
A = [(z*norm)%P for z in A]
A[0] = (A[0]-1)%P
WHT(A)

# Constructeur style déclaration C
B = [-1 for _ in range(SZ)]
B[0] = SZ-1
WHT(B)

# Funky composition d'ordre supérieur
def combine(u, v): return (inv(u)*v)%P
C = list(map(combine, A, B))
WHT(C)

for ix in range(SZ):
    C[ix] = C[ix]*inv(SZ)%P

for j in range(SZ):
    print((C[j]-C[0])%P)