import sys

input = sys.stdin.readline

def neighbors(x, y):
    return [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]

while True:
    n = int(input())
    if n == 0:
        break

    heads = set()
    foots = set()
    for _ in range(n):
        x, y, d = input().split()
        x, y = int(x), int(y)
        if d == 'x':
            h = (x, y)
            f = (x+1, y)
        else:
            h = (x, y)
            f = (x, y+1)
        heads.add(h)
        foots.add(f)

    # Check if any foot adjacent to a head (other than his own)
    bad = False
    for f in foots:
        for nb in neighbors(*f):
            if nb in heads:
                if nb not in foots:
                    # nb is a head cell, f is foot of different futon
                    bad = True
                    break
        if bad:
            break

    print("No" if bad else "Yes")