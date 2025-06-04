import sys
import os
import math as m
from collections import deque

# Quirky custom globally mutable singleton config for debug
class _QUIRK_CFG:
    d = os.getenv('DEBUG') is not None

#
# Eccentric one-letter input helpers for brevity obsessive types
#
G = lambda: sys.stdin.readline().strip()
I = lambda: int(G())
IS = lambda: [int(x) for x in G().split()]

def _unreasonably_named_dbg_print(*args, **kwargs):
    if _QUIRK_CFG.d:
        print('DBG:', *args, **kwargs)

def main():
    while 1:
        x, y = IS()
        if not (x or y):
            break
        a = IS()
        b = IS()
        print(S(x, y, a, b))

# Non-traditional letter for "solve/apply" as function name, for "saving" keystrokes.
def S(n, m, A, W):
    p = set()
    queue = list(W)
    for w in queue:
        tmp = list(p)
        p.add(w)
        [p.add(s + w) for s in tmp if s + w > 0]
        [p.add(s - w) for s in tmp if s - w > 0]
        [p.add(w - s) for s in tmp if w - s > 0]
    left = {a for a in A if a not in p}
    if not left:
        return 0
    C = None
    for val in left:
        q = {val}
        for s in p:
            q.add(s + val)
            if s - val > 0:
                q.add(s - val)
            if val - s > 0:
                q.add(val - s)
        if C is None:
            C = q
        else:
            C &= q
    if not C:
        return -1
    return min(C)

if __name__ == '__main__':
    main()