import sys
import math

def can_place_square(x_left, side, circles):
    x_right = x_left + side
    max_below = -math.inf
    for x_c, r in circles:
        if x_c + r < x_left or x_c - r > x_right:
            continue
        dx_left = max(x_left - x_c, -r)
        dx_right = min(x_right - x_c, r)
        dx = max(abs(dx_left), abs(dx_right))
        if dx > r:
            continue
        h = math.sqrt(r*r - dx*dx)
        max_below = max(max_below, -h)
    return max_below + side <= 0

def solve(circles):
    xs = [x for x,_ in circles]
    r_max = max(r for _,r in circles)
    left = 0.0
    right = 2 * (max(xs[-1] - xs[0], r_max) + r_max)
    EPS = 1e-7
    for _ in range(60):
        mid = (left + right) / 2
        # Try all candidates by sweeping from leftmost circle center - radius to rightmost center + radius
        # to check if square can be placed with side = mid
        # To optimize, we try placing the square aligned at each circle center - mid and circle center
        # Because optimal place corresponds to place tangent to island boundary.
        can = False
        # We do a two pointer approach to check coverage intervals and find minimal base
        intervals = []
        for xc, r in circles:
            intervals.append( (xc - r, xc + r) )
        intervals.sort()
        # Merge intervals
        merged = []
        s,e = intervals[0]
        for i in range(1,len(intervals)):
            if intervals[i][0] <= e:
                e = max(e, intervals[i][1])
            else:
                merged.append((s,e))
                s,e = intervals[i]
        merged.append((s,e))
        # Try to place square inside merged intervals
        for s,e in merged:
            if e - s >= mid:
                can = True
                break
        if can:
            left = mid
        else:
            right = mid
    print(left)

input=sys.stdin.readline
while True:
    N=int(input())
    if N==0:
        break
    circles=[tuple(map(int,input().split())) for _ in range(N)]
    solve(circles)