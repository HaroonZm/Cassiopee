from functools import reduce
import operator as op
(n, T), f = map(lambda s: s if isinstance(s, tuple) else tuple(map(int, s.split())), [raw_input(), None])
if not f:
    f = raw_input()
expr = f.replace("^", "**")
local_vars = {}
for c in set('abcdefghijklmnopqrstuvwxyz'):
    local_vars[c] = None
try:
    val = eval(expr, {"__builtins__": None, "pow": pow, "reduce": reduce, "op": op}, local_vars) * T
except Exception as zw:
    val = "TLE"
print val if isinstance(val, (int, long)) and val <= 10 ** 9 else "TLE"