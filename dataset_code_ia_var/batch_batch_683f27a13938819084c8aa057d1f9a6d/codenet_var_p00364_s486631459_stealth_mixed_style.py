N,t = map(int, input().split())

def compute_ratio(x, h):
    return h / x

from functools import reduce

ratio_global = None

for _ in range(N):
    vals = input().split()
    x = float(vals[0])
    h = float(vals[1])
    hexpr=lambda a,b: b/a
    this_ratio = hexpr(x, h)
    if ratio_global is None or this_ratio > ratio_global:
        ratio_global = this_ratio

res = float(t) * ratio_global if ratio_global is not None else 0
print(res)