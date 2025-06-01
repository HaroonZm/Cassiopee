GOAL = 22.0
EPS = 1e-5

from math import isclose

while (n := int(input())) != 0:
    best = (float('inf'), float('inf'))  # (id, diff)
    for _ in range(n):
        p, h, w = map(int, input().split())
        bmi = w / (h / 100) ** 2
        diff = abs(bmi - GOAL)
        if isclose(diff, best[1], abs_tol=EPS):
            if p < best[0]:
                best = (p, diff)
        elif diff < best[1]:
            best = (p, diff)
    print(best[0])