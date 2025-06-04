import sys
import math
from shapely.geometry import Polygon, Point
from shapely.ops import unary_union

input=sys.stdin.readline

n,r=map(int,input().split())
pts=[tuple(map(int,input().split())) for _ in range(n)]
poly=Polygon(pts)

def area_at(cx,cy):
    circle=Point(cx,cy).buffer(r, resolution=64)
    inter=poly.intersection(circle)
    return inter.area if not inter.is_empty else 0

# Candidate centers: polygon vertices and polygon vertices with circle radius in all directions
candidates=pts[:]
for x,y in pts:
    for dx,dy in [(r,0),(-r,0),(0,r),(0,-r)]:
        cx,cy=x+dx,y+dy
        # inside polygon convex hull bounding box
        if 0<=cx<=100 and 0<=cy<=100:
            candidates.append((cx,cy))
# Also add polygon centroid
cent=poly.centroid
candidates.append((cent.x,cent.y))

best=0
for cx,cy in candidates:
    val=area_at(cx,cy)
    if val>best:
        best=val

# local refinements around best centers
# use grid search with decreasing step size around candidates with high area

def local_search(x0,y0):
    step=5.0
    best_area=0
    best_x,best_y = x0,y0
    for it in range(5):
        for dx in [-step,0,step]:
            for dy in [-step,0,step]:
                nx,ny=best_x+dx,best_y+dy
                if not (0<=nx<=100 and 0<=ny<=100):
                    continue
                a=area_at(nx,ny)
                if a>best_area:
                    best_area=a
                    best_x, best_y = nx, ny
        step/=2
    return best_area, best_x, best_y

improved=0
for cx,cy in candidates:
    a,x,y=local_search(cx,cy)
    if a>best:
        best=a
        improved=1

print(f"{best:.6f}")