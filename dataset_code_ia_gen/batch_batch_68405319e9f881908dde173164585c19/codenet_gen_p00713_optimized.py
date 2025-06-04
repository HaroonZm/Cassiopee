import sys
import math

def dist(a,b):
    return math.hypot(a[0]-b[0],a[1]-b[1])

def centers(p1, p2):
    # circle radius
    r = 1.0
    midx, midy = (p1[0]+p2[0])/2, (p1[1]+p2[1])/2
    d = dist(p1,p2)
    if d > 2*r:
        return []
    # distance from midpoint to circle center
    h = math.sqrt(r*r - (d/2)*(d/2))
    dx, dy = (p2[0]-p1[0])/d, (p2[1]-p1[1])/d
    # two centers, one on each side of line p1-p2
    c1 = (midx - dy*h, midy + dx*h)
    c2 = (midx + dy*h, midy - dx*h)
    return [c1,c2]

def solve(points):
    n = len(points)
    if n == 1:
        return 1
    max_count = 1
    # Check each point as center
    for p in points:
        count = 0
        for q in points:
            if dist(p,q) <= 1.0000001:
                count += 1
        if count > max_count:
            max_count = count
    # Check circles passing through pairs of points
    for i in range(n):
        for j in range(i+1,n):
            for c in centers(points[i], points[j]):
                count = 0
                for k in range(n):
                    if dist(c, points[k]) <= 1.0000001:
                        count += 1
                if count > max_count:
                    max_count = count
    return max_count

def main():
    input = sys.stdin.readline
    while True:
        line = input()
        if not line:
            break
        N = line.strip()
        if N == '0':
            break
        N = int(N)
        points = [tuple(map(float, input().split())) for _ in range(N)]
        print(solve(points))

if __name__ == '__main__':
    main()