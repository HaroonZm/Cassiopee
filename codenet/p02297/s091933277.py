import math
import cmath

def area(b,c):
    theta = cmath.phase(b)
    C = (c)*complex(math.cos(-theta),math.sin(-theta))
    return abs(b)*C.imag/2

n = int(input())
P = []
for i in range(n):
    x,y = map(float,input().split())
    P.append(complex(x,y))
P.append(P[0])
N = len(P)
total = 0.0
for i in range(0,N-1):
    b,c = P[i],P[i+1]
    total += area(b,c)

print(round(total,1))