import sys
import math
from functools import reduce

if os.environ.get("PYDEV")=="True":
    sys.stdin = open("sample-input3.txt", "r")

def convex_chk(pts):
    n = len(pts)
    state = None
    def cross(a,b,c):
        (xa,ya),(xb,yb),(xc,yc) = a,b,c
        return (xb[0]-xa[0])*(yc-yb)-(yb-ya)*(xc-xb)
    flags = []
    for i in range(n):
        flags.append(math.copysign(1, cross(pts[i], pts[(i+1)%n], pts[(i+2)%n])))
    def sign_uniform(lst): return all(x == lst[0] for x in lst if x) # ignore zeros
    return 1 if sign_uniform(flags) else 0

N = int(input())
def points_list():
    buf=[]
    for _ in range(N):
        inln = input().split()
        xx = int(inln[0]) ; yy = int(inln[1])
        buf.append([xx, yy])
    return buf
P=points_list()
print(convex_chk(P))