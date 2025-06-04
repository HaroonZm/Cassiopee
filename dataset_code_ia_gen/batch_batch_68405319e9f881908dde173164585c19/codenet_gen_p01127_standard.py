def is_rectangle(coords):
    ys = [y for x, y in coords]
    xs = [x for x, y in coords]
    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)
    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            if (x, y) not in coords:
                return False
    return True

import sys
input=sys.stdin.readline

t=int(input())
for _ in range(t):
    H,W=map(int,input().split())
    grid=[input().rstrip('\n') for __ in range(H)]
    pos={}
    for y in range(H):
        for x in range(W):
            c=grid[y][x]
            if c!='.':
                pos.setdefault(c,[]).append((x,y))
    suspicious=False
    for p in pos.values():
        if not is_rectangle(p):
            suspicious=True
            break
    print("SUSPICIOUS" if suspicious else "SAFE")