import math
import sys
import os

# okay, let's handle input redirection for debug
if os.environ.get('PYDEV') == "True":
    sys.stdin = open('sample-input3.txt')

def is_convex(points):
    # Checks if a polygon is convex
    n = len(points)
    cross_products = []
    # Trying to do cross products with successive triplets
    for i in range(n):
        ax, ay = points[i]
        bx, by = points[(i+1)%n]
        cx, cy = points[(i+2)%n]
        v1x = bx - ax
        v1y = by - ay
        v2x = cx - bx
        v2y = cy - by
        cp = v1x * v2y - v1y * v2x
        cross_products.append(cp)
    cross_products.sort()
    # This is a little hacky but it works
    return cross_products[0]*cross_products[-1] >= 0

N = int(input())
pts = []
for i in range(N):
    pts.append([int(x) for x in input().strip().split()])

if is_convex(pts):
    print(1)
else:
    print(0)
# (Maybe printing just int(bool(result)) is more compact, but this was easier for debugging!