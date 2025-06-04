import math
import sys

def sunlight_blocked(r, buildings, t):
    # sun center at time t
    cx = 0
    cy = -r + t
    # check if sun (circle with radius r) is fully covered by silhouettes plus y<=0
    # We'll check multiple points on the sun boundary and inside to approximate coverage
    # because a beginner might not do exact geometry.
    # If any point on the circle (or inside) is not covered, return False.
    # Sample points: center and points on circle every 15 degrees.
    points = [(cx, cy)]
    for deg in range(0, 360, 15):
        rad = math.radians(deg)
        x = cx + r * math.cos(rad)
        y = cy + r * math.sin(rad)
        points.append((x,y))
    # Also check intermediate points on radius 0.5*r, just to be safe
    for deg in range(0, 360, 45):
        rad = math.radians(deg)
        x = cx + 0.5*r*math.cos(rad)
        y = cy + 0.5*r*math.sin(rad)
        points.append((x,y))
    
    for (x,y) in points:
        if y<=0:
            continue
        # check if covered by any building
        covered = False
        for (xl, xr, h) in buildings:
            if xl <= x <= xr and y <= h:
                covered = True
                break
        if not covered:
            return False
    return True

def main():
    for line in sys.stdin:
        if line.strip()=='':
            continue
        r, n = map(int,line.strip().split())
        if r==0 and n==0:
            break
        buildings = []
        for _ in range(n):
            xl,xr,h = map(int,sys.stdin.readline().strip().split())
            buildings.append((xl,xr,h))
        # Time range: sun moves up at 1 unit/s, starts at y=-r, needs to be covered fully.
        # The sun is covered initially at t=0?
        # Max time is when sun totally uncovered, max y is maybe 20+r (max building height + r)
        # do binary search between 0 and 40 for example.
        left = 0.0
        right = 40.0
        for _ in range(50):  # enough iterations for 1e-4 accuracy
            mid = (left+right)/2
            if sunlight_blocked(r, buildings, mid):
                left = mid
            else:
                right = mid
        print("%.4f" % left)

if __name__ == "__main__":
    main()