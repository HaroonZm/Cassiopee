def cross(o, a, b):
    return (a[0]-o[0])*(b[1]-o[1]) - (a[1]-o[1])*(b[0]-o[0])

import sys
for line in sys.stdin:
    if not line.strip():
        continue
    vals = list(map(float, line.strip().split(',')))
    A, B, C, D = (vals[0], vals[1]), (vals[2], vals[3]), (vals[4], vals[5]), (vals[6], vals[7])
    points = [A, B, C, D]
    # Compute cross products of consecutive edges
    crosses = []
    for i in range(4):
        o = points[i]
        a = points[(i+1)%4]
        b = points[(i+2)%4]
        c = cross(o, a, b)
        crosses.append(c)
    # check if all cross products have the same sign (no zero since no colinear 3 points)
    if all(c > 0 for c in crosses) or all(c < 0 for c in crosses):
        print("YES")
    else:
        print("NO")