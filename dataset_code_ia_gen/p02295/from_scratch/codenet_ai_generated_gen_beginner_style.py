q = int(input())
for _ in range(q):
    x0, y0, x1, y1, x2, y2, x3, y3 = map(int, input().split())
    
    # Line s1 represented as p0 + t*(p1-p0)
    # Line s2 represented as p2 + u*(p3-p2)
    # We solve for t and u where the lines intersect:
    
    dx1 = x1 - x0
    dy1 = y1 - y0
    dx2 = x3 - x2
    dy2 = y3 - y2
    
    # Equation system:
    # x0 + t*dx1 = x2 + u*dx2
    # y0 + t*dy1 = y2 + u*dy2
    
    # Rearranged:
    # t*dx1 - u*dx2 = x2 - x0
    # t*dy1 - u*dy2 = y2 - y0
    
    # Solve for t using Cramer's rule
    denom = dx1 * dy2 - dy1 * dx2
    
    t = ((x2 - x0) * dy2 - (y2 - y0) * dx2) / denom
    
    ix = x0 + t * dx1
    iy = y0 + t * dy1
    
    print("%.10f %.10f" % (ix, iy))