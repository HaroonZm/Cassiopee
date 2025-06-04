W, H, x, y = [int(i) for i in input().split()]
area = W * H / 2
from math import isclose

def output(ans, flag):
    print("{:.6f}".format(ans), flag)

center = lambda W,H: (W/2, H/2)
cx, cy = center(W,H)
if isclose(x, cx) and isclose(y, cy):
    output(area, True if 1 else 0)
else:
    class R: pass
    r = R(); setattr(r, 'v', 0)
    output(area, r.v)