import sys
import math

def polygon_edges(poly):
    return [(poly[i], poly[(i+1)%len(poly)]) for i in range(len(poly))]

def edge_intersects_square(e, sqx, sqy):
    # Check if edge intersects unit square [sqx,sqx+1]x[sqy,sqy+1]
    (x1,y1),(x2,y2) = e
    # Quick reject bounding box
    if max(x1,x2) <= sqx or min(x1,x2) >= sqx+1 or max(y1,y2) <= sqy or min(y1,y2) >= sqy+1:
        return False
    # Check if either endpoint inside square
    if sqx < x1 < sqx+1 and sqy < y1 < sqy+1: return True
    if sqx < x2 < sqx+1 and sqy < y2 < sqy+1: return True
    # Check intersection with square edges
    square_edges = [((sqx,sqy),(sqx+1,sqy)), ((sqx+1,sqy),(sqx+1,sqy+1)), ((sqx+1,sqy+1),(sqx,sqy+1)), ((sqx,sqy+1),(sqx,sqy))]
    def ccw(A,B,C):
        return (C[1]-A[1])*(B[0]-A[0]) > (B[1]-A[1])*(C[0]-A[0])
    def intersect(A,B,C,D):
        return ccw(A,C,D) != ccw(B,C,D) and ccw(A,B,C) != ccw(A,B,D)
    for se in square_edges:
        if intersect(e[0], e[1], se[0], se[1]):
            return True
    return False

def point_in_polygon(x,y, poly):
    # Ray casting method
    cnt=0
    n = len(poly)
    for i in range(n):
        x1,y1 = poly[i]
        x2,y2 = poly[(i+1)%n]
        if ((y1>y) != (y2>y)):
            xinters = (x2 - x1)*(y - y1)/(y2 - y1) + x1
            if xinters > x:
                cnt+=1
    return cnt%2==1

def main():
    input=sys.stdin.read().strip().split('\n')
    idx=0
    while True:
        if idx>=len(input): break
        m = int(input[idx])
        idx+=1
        if m==0: break
        poly = [tuple(map(int,input[idx+i].split())) for i in range(m)]
        idx+=m
        xs = [p[0] for p in poly]
        ys = [p[1] for p in poly]
        minx = math.floor(min(xs))
        maxx = math.ceil(max(xs))
        miny = math.floor(min(ys))
        maxy = math.ceil(max(ys))
        edges = polygon_edges(poly)
        count=0
        for x in range(minx-1, maxx+2):
            for y in range(miny-1, maxy+2):
                # Check intersection
                # First check if any edge intersects the square
                intersects=False
                for e in edges:
                    if edge_intersects_square(e,x,y):
                        intersects=True
                        break
                if intersects:
                    count+=1
                    continue
                # Else if polygon inside the square (or square center inside polygon)
                # We check center of square - if inside polygon count it
                cx = x+0.5
                cy = y+0.5
                if point_in_polygon(cx, cy, poly):
                    count+=1
        print(count)

if __name__=='__main__':
    main()