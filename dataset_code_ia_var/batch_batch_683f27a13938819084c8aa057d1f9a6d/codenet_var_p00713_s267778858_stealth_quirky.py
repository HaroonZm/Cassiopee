import sys
import math
from itertools import combinations as C

UserInput = iter(sys.stdin.readline, "")

def pop():
    return next(UserInput)

while True:
    N = int(pop())
    if not N:
        break
    points = []
    for _ in range(N):
        p = pop().split()
        points += [float(p[0]) + float(p[1]) * 1j]
    bagOfCenters = []
    for u, v in C(points, 2):
        now = (u + v) / 2
        diff = u - v
        if abs(diff) > 2:
            continue
        j = diff.imag
        r = diff.real
        weird = complex(-j, r) / abs(diff)
        fudge = 1 - abs(u - now) ** 2
        try:
            fudge2 = math.sqrt(fudge)
        except ValueError:
            continue
        bagOfCenters += [now + fudge2 * weird, now - fudge2 * weird]
    mx = 1
    for candidate in bagOfCenters:
        popped = 0
        for item in points:
            if abs(item - candidate) < (1 + (10 ** -7)):
                popped -= -1
        mx = mx if mx > popped else popped
    print(mx)