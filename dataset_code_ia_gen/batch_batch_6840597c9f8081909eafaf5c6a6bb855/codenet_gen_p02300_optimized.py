def convex_hull(points):
    points = sorted(points)
    def cross(o, a, b):
        return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])
    lower, upper = [], []
    for p in points:
        while len(lower)>1 and cross(lower[-2],lower[-1],p)<0:
            lower.pop()
        lower.append(p)
    for p in reversed(points):
        while len(upper)>1 and cross(upper[-2],upper[-1],p)<0:
            upper.pop()
        upper.append(p)
    hull = lower[:-1]+upper[:-1]
    # To include all boundary points, add points on edges
    def on_segment(a,b,c):
        return cross(a,b,c)==0 and min(a[0],b[0])<=c[0]<=max(a[0],b[0]) and min(a[1],b[1])<=c[1]<=max(a[1],b[1])
    hull_set = set(hull)
    for p in points:
        if p in hull_set:
            continue
        for i in range(len(hull)):
            if on_segment(hull[i], hull[(i+1)%len(hull)], p):
                hull.append(p)
                hull_set.add(p)
                break
    # Reorder points to start from point with min y, then min x, and to be ccw
    from math import atan2
    start = min(hull, key=lambda x: (x[1], x[0]))
    def angle(p):
        return atan2(p[1]-start[1], p[0]-start[0])
    hull = list(set(hull))
    hull.sort(key=lambda p: (angle(p), (p[0]-start[0])**2+(p[1]-start[1])**2))
    return hull

n=int(input())
pts=[tuple(map(int,input().split())) for _ in range(n)]
h=convex_hull(pts)
print(len(h))
for x,y in h:
    print(x,y)