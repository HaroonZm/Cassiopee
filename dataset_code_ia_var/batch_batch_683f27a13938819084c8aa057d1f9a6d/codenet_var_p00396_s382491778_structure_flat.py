from collections import defaultdict
import sys

sys.setrecursionlimit(1000000)
mod = 1000000007

g = defaultdict(lambda : None)
g[(0,0)] = 0

# Lire le nombre de cas
n = int(sys.stdin.readline())
ans = 0

# Minimiser les fonctions, tout en ligne
for _ in range(n):
    w, b = map(int, sys.stdin.readline().split())
    stack = []
    visited = []
    local_stack = [(w, b)]
    while local_stack:
        ww, bb = local_stack[-1]
        if g[(ww, bb)] is not None:
            local_stack.pop()
            continue
        calc_needed = False
        s = set()
        if ww:
            if g[(ww-1, bb)] is None:
                local_stack.append((ww-1, bb))
                calc_needed = True
            else:
                s.add(g[(ww-1, bb)])
        if bb:
            if g[(ww+1, bb-1)] is None:
                local_stack.append((ww+1, bb-1))
                calc_needed = True
            else:
                s.add(g[(ww+1, bb-1)])
        for i in range(1, min(ww, bb)+1):
            if g[(ww, bb-i)] is None:
                local_stack.append((ww, bb-i))
                calc_needed = True
            else:
                s.add(g[(ww, bb-i)])
        if calc_needed:
            continue
        i = 0
        while i in s:
            i += 1
        g[(ww, bb)] = i
        local_stack.pop()
    ans ^= g[(w, b)]

if ans:
    print(0)
else:
    print(1)