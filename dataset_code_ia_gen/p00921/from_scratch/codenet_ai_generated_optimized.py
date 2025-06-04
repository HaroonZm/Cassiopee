import sys
import math

def dist(a, b):
    return math.hypot(a[0]-b[0], a[1]-b[1])

def feasible(r, w, needles):
    # The balloon radius is r, it sits on z=0
    # Check if there's a position (x,y) inside [r,100-r] square s.t
    # for any needle (xi,yi,hi): (hi)^2 + (distance to balloon center)^2 >= (r)^2 (balloon won't penetrate needles)
    # For all walls: x in [r,100-r], y in [r,100-r]
    # To check feasibility, test candidate points
    # We will try candidate points as:
    # center at (r, r), at (r, 100 - r), at (100 - r, r), at (100 - r, 100 - r)
    # and needle points' coordinates adjusted by distance r in directions
    
    # Also, as n small, try all points where balloon touches:
    # balloon touches floor at z=0, and must not penetrate needles or walls
    
    # Approach:
    # The balloon center must be at least r away from walls (0 and 100)
    # For each needle at (xi, yi) with height hi, the balloon center must satisfy:
    # distance(center, (xi, yi))^2 >= r^2 - hi^2 if hi < r, else no constraint from that needle
    # Because the balloon is a sphere of radius r resting on z=0
    # Its center is at (x, y, r)
    # The needle extends from (xi, yi, 0) to (xi, yi, hi)
    # Balloon surface is (x-xc)^2 + (y-yc)^2 + (z-r)^2 = r^2
    # For needle endpoint (xi, yi, hi), distance to center >= r (to avoid intersection)
    # So (xi - x)^2 + (yi - y)^2 + (hi - r)^2 >= r^2 =>
    # (xi - x)^2 + (yi - y)^2 >= r^2 - (hi - r)^2 = r^2 - (hi^2 -2*hi*r + r^2) = 2*hi*r - hi^2
    # If 2*hi*r - hi^2 < 0, no constraint (needle higher than ball radius), else:
    # distance^2 >= 2 * hi * r - hi^2
    
    # Let's define for each needle a forbidden disk with radius sqrt(2*hi*r - hi^2) centered on (xi, yi).
    # The balloon center must lie outside all forbidden disks and inside box with margin r.
    
    # Search for a position within [r,100-r]^2 outside forbidden disks
    
    forbidden = []
    for (xi, yi, hi) in needles:
        val = 2*hi*r - hi*hi
        if val > 0:
            forbidden.append((xi, yi, math.sqrt(val)))
    # If no forbidden disks, balloon center can be anywhere inside box in [r,100-r]^2
    
    # Check feasibility by attempting to find a point in [r, 100-r]^2 outside all forbidden disks
    # Because n is small, try candidate points:
    # 1) Try centers at the 4 corners: (r, r), (r, 100-r), (100-r, r), (100-r, 100-r)
    # 2) For each forbidden disk, try points shifted away from the disk center by its radius + epsilon in 8 directions
    candidates = [(r, r), (r, 100-r), (100-r, r), (100-r, 100-r)]
    for (cx, cy, cr) in forbidden:
        # try points around this forbidden disk margin
        for dx, dy in [(1,0), (-1,0), (0,1),(0,-1), (1,1), (1,-1), (-1,1), (-1,-1)]:
            norm = math.hypot(dx, dy)
            nx = cx + (cr + 1e-7) * dx / norm
            ny = cy + (cr + 1e-7) * dy / norm
            if r <= nx <= 100 - r and r <= ny <= 100 - r:
                candidates.append((nx, ny))
                
    def ok(x,y):
        # Check walls
        if not (r <= x <= 100 - r and r <= y <= 100 - r):
            return False
        # Check needles
        for (xi, yi, hi) in needles:
            val = 2*hi*r - hi*hi
            if val > 0:
                d2 = (x - xi)**2 + (y - yi)**2
                if d2 < val - 1e-14:
                    return False
        return True
    
    for (x,y) in candidates:
        if ok(x,y):
            return True
    return False

def main():
    input = sys.stdin.readline
    while True:
        line = input()
        if not line:
            break
        n,w = map(int, line.strip().split())
        if n == 0 and w == 0:
            break
        needles = []
        for _ in range(n):
            xi, yi, hi = map(int, input().split())
            needles.append((xi, yi, hi))
        # Binary search radius r from 0 to min(50, w)
        # Max r limited by box height w (balloon radius cannot exceed wall height)
        # Also r must ≤ 50 by box floor constraints (distance to walls)
        lo, hi = 0.0, min(w,50.0)
        for _ in range(60):
            mid = (lo+hi)/2
            if feasible(mid, w, needles):
                lo = mid
            else:
                hi = mid
        print(f"{lo:.5f}")

if __name__=="__main__":
    main()