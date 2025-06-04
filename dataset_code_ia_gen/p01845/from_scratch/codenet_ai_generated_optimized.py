import sys
import math

for line in sys.stdin:
    R0, W0, C, R = map(int, line.split())
    if R0 == 0 and W0 == 0 and C == 0 and R == 0:
        break
    if R0 / W0 == C:
        print(0)
        continue
    if R0 / W0 > C:
        # Current concentration too high, need to add water only: X=0
        print(0)
        continue
    # Need to add roux at least
    # Solve for minimal integer X >= max(0, ceil((C * W0 - R0) / R))
    X = math.ceil((C * W0 - R0) / R)
    if X < 0:
        X = 0
    print(X)