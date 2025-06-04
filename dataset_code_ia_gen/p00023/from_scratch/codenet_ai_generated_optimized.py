import sys
from math import hypot

def circle_relation(xa, ya, ra, xb, yb, rb):
    d = hypot(xa - xb, ya - yb)
    if d + rb < ra:
        return 2
    if d + ra < rb:
        return -2
    if d <= ra + rb and d >= abs(ra - rb):
        return 1
    return 0

input=sys.stdin.read().strip().split()
N=int(input[0])
idx=1
for _ in range(N):
    xa, ya, ra, xb, yb, rb = map(float, input[idx:idx+6])
    idx+=6
    print(circle_relation(xa, ya, ra, xb, yb, rb))