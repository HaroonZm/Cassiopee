import sys
import math

input = sys.stdin.readline

def can_place(S, xs, rs):
    max_left = xs[0] - rs[0]
    max_right = xs[0] + rs[0]
    min_top = rs[0]
    max_height = 0
    y_max = rs[0]
    n = len(xs)
    for i in range(n):
        y_max = max(y_max, rs[i])
    # We try to place a square of side S somewhere so that it fits inside the island.
    # Since the island is union of circles centered on x-axis,
    # For a candidate bottom yb, the vertical bound is circle_y_bound = sqrt(r^2 - (x - cx)^2)
    # For bottom yb, the square covers [x0, x0+S] in x and [yb, yb+S] in y.
    # We need for all x in [x0, x0+S], yb+S <= circle_y_bound(x)
    # We binary search x0 between xs[0]-max_r and xs[-1]+max_r - S.
    left = xs[0] - rs[0]
    right = xs[-1] + rs[-1]
    # We'll try all possible x positions where the square can fit within island's horizontal range
    # But to be efficient, do binary search on x0 for placing square horizontally.
    lo = left
    hi = right - S
    if hi < lo:
        return False
    for _ in range(50):
        mid = (lo + hi) / 2
        # We check if bottom can be placed so the square fits in island at x in [mid, mid+S]
        # max height of island inside the horizontal interval of the square must be >= S
        # Let's find the minimal vertical distance between the top boundary of island and bottom (yb),
        # actually we want max of minimal yb so that top is >= yb+S
        # Equivalently, find min among all points in [mid,mid+S] of circle_y_bound(x)
        min_top_bound = float('inf')
        # Since xs and rs large, precompute circle coverage for these points efficiently
        # We'll intersect each circle with square horizontal segment [mid,mid+S] 
        # and take min of circle_y_bound(x) over this segment
        # Because circles may overlap, minimal over union is the maximum y for each x
        # So minimal top bound is min over x in [mid, mid+S] of max over circles of y(x)
        # Approximate by sampling points
        M = 20
        feasible = True
        for j in range(M+1):
            x = mid + S * j / M
            max_h = -1
            # For each circle check if x in circle projection horizontally:
            # circle covers x if |x - cx| <= r
            # then y = sqrt(r^2 - (x - cx)^2)
            # max_h is max over all circles
            # We'll use binary search to find nearby circles
            # Since centers sorted, find left bound where center cx >= x - max_r
            # but max_r up to 1e5, so traversal cost may be high
            # Let's do with binary search:
            from bisect import bisect_left
            idx = bisect_left(xs, x)
            candidates = []
            if idx < n:
                candidates.append(idx)
            if idx > 0:
                candidates.append(idx-1)
            # For safety check neighbors around idx
            for k in candidates:
                dx = abs(xs[k]-x)
                if dx <= rs[k]:
                    h = math.sqrt(rs[k]*rs[k] - dx*dx)
                    if h > max_h:
                        max_h = h
            if max_h < S:
                feasible = False
                break
        if feasible:
            hi = mid
        else:
            lo = mid
    return hi < right

def main():
    while True:
        N = int(sys.stdin.readline())
        if N == 0:
            break
        xs = []
        rs = []
        for _ in range(N):
            x,r = map(int, sys.stdin.readline().split())
            xs.append(x)
            rs.append(r)
        low, high = 0.0, max(rs)*2
        for i in range(N-1):
            dist = xs[i+1] - xs[i]
            # max possible side limited by horizontal gaps and radii
            high = max(high, rs[i]+rs[i+1], dist+min(rs[i], rs[i+1])*2)
        # Binary search largest S
        for _ in range(60):
            mid = (low+high)/2
            if can_place(mid, xs, rs):
                low = mid
            else:
                high = mid
        print(low)

if __name__ == '__main__':
    main()