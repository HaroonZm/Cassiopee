def get_input():
    from sys import stdin
    try:
        line = stdin.readline()
        if not line: return None
        return list(map(int, line.strip().split()))
    except:
        return None

def solve(r0, w0, c, r):
    req = c * w0
    rem = max(0, req - r0)
    if rem % r == 0:
        return rem // r
    return rem // r + 1

import sys

ask = True
while ask:
    vals = None
    if hasattr(__builtins__, 'raw_input'):
        vals = list(map(int, raw_input().split()))
    else:
        vals = get_input()
    if not vals or sum(vals) == 0:
        ask = False
        continue
    res = solve(*vals)
    sys.stdout.write(str(res))
    print