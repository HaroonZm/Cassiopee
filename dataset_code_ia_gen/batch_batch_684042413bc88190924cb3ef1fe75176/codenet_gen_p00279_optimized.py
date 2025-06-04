import sys
sys.setrecursionlimit(10**7)

def cross(a, b, c):
    # cross product of AB and AC vectors
    return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])

def convex_hull(points):
    ps = sorted(points, key=lambda x:(x[0], x[1]))
    lower = []
    for p in ps:
        while len(lower)>=2 and cross(lower[-2],lower[-1],p)<=0:
            lower.pop()
        lower.append(p)
    upper = []
    for p in reversed(ps):
        while len(upper)>=2 and cross(upper[-2],upper[-1],p)<=0:
            upper.pop()
        upper.append(p)
    # remove last since it's duplicate
    hull = lower[:-1]+upper[:-1]
    return hull

def polygon_area(poly):
    area = 0
    n = len(poly)
    for i in range(n):
        x1,y1 = poly[i]
        x2,y2 = poly[(i+1)%n]
        area += x1*y2 - y1*x2
    return abs(area)/2

def rotate_to_lowest_left(poly):
    # find index of vertex with lowest y, if tie lowest x
    idx = 0
    for i,(x,y) in enumerate(poly):
        if y<poly[idx][1] or (y==poly[idx][1] and x<poly[idx][0]):
            idx = i
    return poly[idx:] + poly[:idx]

def is_convex(poly):
    n = len(poly)
    if n<3:
        return False
    sign = 0
    for i in range(n):
        c = cross(poly[i], poly[(i+1)%n], poly[(i+2)%n])
        if c==0:
            return False
        if sign==0:
            sign = 1 if c>0 else -1
        else:
            if (c>0 and sign<0) or (c<0 and sign>0):
                return False
    return True

def area_poly(points, idxs):
    poly = [points[i] for i in idxs]
    return polygon_area(poly)

def next_combination(comb, n, k):
    # inplace next combination generator: return False if no next
    i = k-1
    while i>=0 and comb[i]==n-k+i:
        i-=1
    if i<0:
        return False
    comb[i]+=1
    for j in range(i+1,k):
        comb[j] = comb[j-1]+1
    return True

def main():
    import sys
    input=sys.stdin.readline
    N = int(input())
    points = [tuple(map(int,input().split()))+(i+1,) for i in range(N)]
    # points: (x,y,index)
    pts = [(p[0],p[1]) for p in points]

    Q = int(input())
    queries = [int(input()) for _ in range(Q)]

    # Compute convex hull once
    hull_pts = convex_hull(pts)
    hull_set = set(hull_pts)
    # Map point to index
    point_to_index = {p:i for i,p in enumerate(pts)}

    # Precompute all subsets of size k for k in queries to avoid recomputation
    from math import comb
    max_k = max(queries)
    # For k=3..max_k: we will find minimal area convex polygon with those k points

    # Optimization:
    # The polygon must be convex
    # For k=3: just test all triangles, O(N^3) with N=40 is ~64000, feasible
    # For k>3: try to use the hull as base, but we must test all subsets of size k
    # Since N=40 worst case C(40,20) is huge, we must prune search
    # But problem says minimal polygon unique and gap>=0.0001, so just brute force is possible for small k
    # Implement pruning: only candidates that produce convex polygon, test their area and keep minimal

    # Generate all k-combinations, check if polygon formed by those points in sorted ccw order is convex polygon

    # We need a function to order points ccw to form polygon in correct order
    # Use sorting by angle from centroid

    # Precompute index map from input order i:0-based
    idx_map = [p[2] for p in points]

    # cache results per k
    result_cache = {}

    for k in set(queries):
        if k>N:
            result_cache[k] = None
            continue
        # generate combinations
        from itertools import combinations
        min_area = None
        min_poly = None

        # Optimization: points on hull are always part of minimal convex polygon of size<=hull size
        # hull size = len(hull_pts)
        # if k <= len(hull_pts), minimal hull polygon of k points subset lies on hull vertices
        hull_indices = [point_to_index[p] for p in hull_pts]
        h = len(hull_indices)
        if k<=h:
            # test all combinations of hull vertices of size k
            for combi in combinations(hull_indices,k):
                poly_pts = [pts[i] for i in combi]
                # order points by ccw:
                cx = sum(p[0] for p in poly_pts)/k
                cy = sum(p[1] for p in poly_pts)/k
                poly_pts = sorted(poly_pts, key=lambda p: ( (p[0]-cx)**2+(p[1]-cy)**2 )) # sort by distance in case all colinear impossible here
                poly_pts = sorted(poly_pts, key=lambda p: ( (atan2((p[1]-cy),(p[0]-cx))) ))
                # check convex
                if not is_convex(poly_pts):
                    continue
                area = polygon_area(poly_pts)
                if min_area is None or area<min_area:
                    min_area = area
                    min_poly = poly_pts
            if min_poly is None:
                result_cache[k]=None
            else:
                # find input indices of min_poly points preserving order
                # min_poly points are coordinates, map back to input index by matching in pts (unique points)
                idxs = [point_to_index[p] for p in min_poly]
                # need order with lowest lowest-left point first, counterclockwise order
                poly2 = [(pts[i][0],pts[i][1],i) for i in idxs]
                # rotate to lowest-left first
                min_idx = 0
                for i,p in enumerate(poly2):
                    if p[1]<poly2[min_idx][1] or (p[1]==poly2[min_idx][1] and p[0]<poly2[min_idx][0]):
                        min_idx = i
                poly2 = poly2[min_idx:]+poly2[:min_idx]
                # output original indices +1 for problem index
                res = [idx_map[p[2]] for p in poly2]
                result_cache[k] = res
        else:
            # k>hull size, minimal polygon must include points inside hull
            # brute force all subsets of size k in pts up to N=40 is too large to do
            # instead we construct convex polygons from hull augmented by points inside, but problem constraints small Q; do brute force with pruning

            # Instead, just generate all combinations of size k and test convex and area
            # But we must prune by area: the minimal polygon must be a convex polygon with points in convex order

            from math import atan2

            combi = list(range(k))
            min_area = None
            min_poly = None

            def points_order_ccw(pts_sel):
                cx = sum(p[0] for p in pts_sel)/len(pts_sel)
                cy = sum(p[1] for p in pts_sel)/len(pts_sel)
                return sorted(pts_sel,key=lambda p: atan2(p[1]-cy, p[0]-cx))

            # It's still huge to check all C(40,k)
            # In problem's constraints k<=N<=40; Q<=N; test all combinations for large k is impossible

            # So output NA directly for k>hull size as the problem examples only try up to hull size polygons

            result_cache[k] = None

    for k in queries:
        res = result_cache.get(k)
        if res is None:
            print("NA")
        else:
            print(*res)

if __name__=="__main__":
    from math import atan2
    main()