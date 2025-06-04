from collections import defaultdict
from collections import deque
from heapq import heappush, heappop
import sys
import math
import bisect
import random

sys.setrecursionlimit(1000000)
mod = 1000000007

# === DEBUT du code principal ===

# Appel E() à l'origine
a, b, c, n = map(int, sys.stdin.readline().split())
dxyz = [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
s = [0 for _ in range(7)]
k = (a==1)+(b==1)+(c==1)

# Calcul surface/volume initial selon le cas de dégénération
if k == 0:
    s[1] = 2*(max(0,a-2)*max(0,b-2)+max(0,c-2)*max(0,b-2)+max(0,a-2)*max(0,c-2))
    s[2] = 4*(max(0,a-2)+max(0,b-2)+max(0,c-2))
    s[3] = 8
elif k == 1:
    s[2] = max(0,a-2)*max(0,b-2)+max(0,c-2)*max(0,b-2)+max(0,a-2)*max(0,c-2)
    s[3] = 2*(max(0,a-2)+max(0,b-2)+max(0,c-2))
    s[4] = 4
elif k == 2:
    s[4] = max(0,a-2)+max(0,b-2)+max(0,c-2)
    s[5] = 2
else:
    s[6] = 1

f = defaultdict(int)

def _surface(x, y, z, a, b, c, k):
    return ((x==0)|(x==a-1))+((y==0)|(y==b-1))+((z==0)|(z==c-1))+k

for _ in range(n):
    x, y, z = map(int, sys.stdin.readline().split())
    s[_surface(x,y,z,a,b,c,k)] -= 1
    f[(x,y,z)] = -1
    for dx, dy, dz in dxyz:
        nx, ny, nz = x+dx, y+dy, z+dz
        if f[(nx,ny,nz)] != -1:
            f[(nx,ny,nz)] += 1

ans = 0
for (x,y,z), j in f.items():
    if j != -1:
        if 0 <= x < a and 0 <= y < b and 0 <= z < c:
            val_surface = _surface(x,y,z,a,b,c,k)
            ans += j+val_surface
            s[val_surface] -= 1

for i in range(1,7):
    ans += i*s[i]

print(ans)