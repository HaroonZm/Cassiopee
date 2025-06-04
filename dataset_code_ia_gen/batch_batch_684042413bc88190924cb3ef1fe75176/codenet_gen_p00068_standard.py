import sys
def cross(o, a, b):
    return (a[0]-o[0])*(b[1]-o[1]) - (a[1]-o[1])*(b[0]-o[0])

def convex_hull(points):
    points = sorted(points)
    lower, upper = [], []
    for p in points:
        while len(lower)>=2 and cross(lower[-2], lower[-1], p)<=0:
            lower.pop()
        lower.append(p)
    for p in reversed(points):
        while len(upper)>=2 and cross(upper[-2], upper[-1], p)<=0:
            upper.pop()
        upper.append(p)
    return lower[:-1]+upper[:-1]

for line in sys.stdin:
    n=line.strip()
    if not n.isdigit():
        continue
    n=int(n)
    if n==0:
        break
    pts=[]
    for _ in range(n):
        x,y=input().strip().split(',')
        pts.append((float(x),float(y)))
    hull=convex_hull(pts)
    hull_set=set(hull)
    print(n - len(hull_set))