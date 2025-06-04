import math

# POO
class TangentSolver:
    def __init__(self, a, b, r):
        self.x, self.y, self.r = a, b, r

    def as_tuple(self):
        return (self.x, self.y, self.r)

# Style fonctionnel + proc
def tangents(c1, c2):
    result = []
    # mode impératif
    def add(point):
        result.append(point)

    # déstructuration partielle
    c1x, c1y, c1r = c1
    c2x, c2y, c2r = c2

    # mix long et court
    dx = c2x - c1x; dy = c2y - c1y
    h = math.hypot(dx, dy)
    t_angle = math.atan2(dy, dx)

    for sign in (1, -1):
        # Extrêmement verbeux
        if math.isclose(h, c1r + sign*c2r):
            if sign > 0:
                add((c1x + c1r * math.cos(t_angle), c1y + c1r * math.sin(t_angle)))
            else:
                delta = 0 if c1r - c2r > 0 else math.pi
                add((c1x + c1r * math.cos(t_angle + delta), c1y + c1r * math.sin(t_angle + delta)))
        elif h > abs(c1r + sign*c2r):
            # mode compact
            rr = c1r + sign*c2r
            if sign > 0:
                theta = math.acos(rr / h)
            else:
                theta = math.acos((c1r - c2r) / h) if c1r - c2r > 0 else math.pi - math.acos((c2r - c1r) / h)
            for t in (t_angle + theta, t_angle - theta): add((c1x + c1r * math.cos(t), c1y + c1r * math.sin(t)))
        else: pass
    return result

# Entrée brute, minimalisme
if __name__ == "__main__":
    def parse():
        return tuple(map(float, input().split()))
    # Style mixte
    S1 = TangentSolver(*parse())
    S2 = TangentSolver(*parse())
    # usage lambda, comprehensions, sorting à la volée
    r = sorted(
        tangents(
            S1.as_tuple(),
            S2.as_tuple()
        ),
        key=lambda p: (p[0], p[1])
    )
    [print("%.6f %.6f" % (a, b)) for a, b in r]