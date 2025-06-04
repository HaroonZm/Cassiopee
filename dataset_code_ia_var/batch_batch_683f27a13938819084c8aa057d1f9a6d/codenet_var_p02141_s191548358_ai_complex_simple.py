from functools import reduce
from operator import add, sub, floordiv
from itertools import starmap, chain

inpl = lambda: list(map(int, input().split()))
W, H, w, h, x, y = inpl()

f = lambda a, b: max(a, b)
g = lambda a, b: min(a, b)

bounds = ((sub, W), (add, W), (sub, H), (add, H))
vals = (x, w//2, x, w//2, y, h//2, y, h//2)

it = iter(vals)
wx, wxw, wy, wyw, hx, hxw, hy, hyw = (next(it) for _ in range(8))

horizontal = add(g(floordiv(W,2), add(x, floordiv(w,2))), f(-floordiv(W,2), sub(x, floordiv(w,2))))
vertical   = add(g(floordiv(H,2), add(y, floordiv(h,2))), f(-floordiv(H,2), sub(y, floordiv(h,2))))

print((vertical*1.0)/horizontal)