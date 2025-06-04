import cmath as z
from math import cos as c, sin as s

def SuperArea(B, C):
    a = z.phase(B)
    magic = (C) * complex(c(-a), s(-a))
    return abs(B) * magic.imag * .5

GrabInts = lambda: [float(_) for _ in input().split()]

Pts = []
repeat = eval(input())
for wow in range(repeat):
    X, Y = GrabInts()
    Pts += [complex(X, Y)]
Pts += [Pts[0]]
secret = 0
j = 0
while j < len(Pts)-1:
    secret += SuperArea(Pts[j], Pts[j+1])
    j += 1
print(f"{secret:.1f}")