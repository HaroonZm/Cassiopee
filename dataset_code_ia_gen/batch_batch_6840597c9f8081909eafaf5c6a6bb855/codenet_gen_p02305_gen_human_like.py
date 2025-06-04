import math

c1x, c1y, c1r = map(int, input().split())
c2x, c2y, c2r = map(int, input().split())

dx = c2x - c1x
dy = c2y - c1y
d = math.hypot(dx, dy)

r1, r2 = c1r, c2r
if r1 > r2:
    r1, r2 = r2, r1

if d == 0:
    # Same center
    if r1 == r2:
        # Circles coincide, problem states c1 and c2 are different, so ignore this case
        print(0)
    else:
        # One circle inside the other with same center => no common tangent line
        print(0)
else:
    if d > r1 + r2:
        # Circles far apart, no intersection, 4 common tangents
        print(4)
    elif d == r1 + r2:
        # Circles touch externally -> 3 common tangents
        print(3)
    elif r2 - r1 < d < r1 + r2:
        # Circles intersect in two points, 2 common tangents
        print(2)
    elif d == r2 - r1:
        # Circles touch internally ('inscribed'), 1 common tangent
        print(1)
    else:
        # One circle includes the other without touching, 0 common tangents
        print(0)