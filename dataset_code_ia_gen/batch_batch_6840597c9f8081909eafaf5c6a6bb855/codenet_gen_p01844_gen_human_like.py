import sys
input = sys.stdin.readline

H, W, N = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(H)]

# 2D prefix sums
s = [[0]*(W+1) for _ in range(H+1)]
for i in range(H):
    for j in range(W):
        s[i+1][j+1] = s[i+1][j] + s[i][j+1] - s[i][j] + a[i][j]

def rect_sum(r1, c1, r2, c2):
    return s[r2][c2] - s[r1][c2] - s[r2][c1] + s[r1][c1]

# We want to maximize the minimum sum among N disjoint rectangles, each rectangle contiguous and non-overlapping

# Since N<=4 and H,W<=200, we try a binary search on the answer
# For a candidate mid, we check if it's possible to partition into N rectangles with each sum >= mid
# We consider only cuts along rows and columns, the partition must be into N rectangles with no overlap
# The approach is to try all partitions into rectangles formed by horizontal and vertical cuts

# We'll consider partitions into rectangles via up to N-1 horizontal cuts and up to N-1 vertical cuts
# For N=2: one cut either horizontal or vertical, forming 2 rectangles
# For N=3: cuts forming 3 rectangles in a line or 2 cuts forming up to 4 rectangles but we pick 3
# For N=4: partitions into 4 rectangles by 1 horizontal and 1 vertical cut (2x2 blocks)
# and other shapes

# Because the problem states "Each brother gets a single rectangular plot"
# The rectangles cannot be overlapping and can be empty but that's allowed (no owner)
# The problem says 0 <= N <=4 (N>=2), and maximum 4 brothers

# We only split to exactly N rectangles, each rectangle assigned to one brother

# We'll try:
# - If N=2: horizontal partition (split rows), or vertical partition (split columns)
# - For N=3: vertical partition into 3 parts (2 vertical cuts), or horizontal partition into 3 parts (2 horizontal cuts),
#            or 1 horizontal + 1 vertical cut to form 4 rectangles, pick 3 rectangles from those 4 to assign?
#   But brothers must get exactly one rectangle each, so we need to consider partitions into exactly N rectangles
#   So 1 horizontal + 1 vertical cut forms 4 rectangles, but N=3 means some brother gets no land (empty) is allowed? Yes
#   So assign 3 of 4 rectangles to brothers, one rectangle discarded
# - For N=4: 2 horizontal cuts and 2 vertical cuts to make 9 rectangles but only 4 to assign? 
#   No, the rectangles must be connected - problem says each brother gets exactly one rectangle (can be empty, but "whoever gets no land is allowed")
#   So empty land is okay, but rectangle assigned to brother must be contiguous rectangle

# So for N=4, the minimal number of rectangles is 4, so we can do cuts to form 4 rectangles:
# e.g. 1 horizontal cut and 1 vertical cut, split into 4 rectangles

# Therefore, we enumerate all possible cut lines making exactly N rectangles, and check if for each rectangle the sum>=mid

def can(N, mid):
    # For N=2: try all horizontal cuts
    if N == 2:
        # horizontal cuts
        for r in range(1, H):
            s1 = rect_sum(0, 0, r, W)
            s2 = rect_sum(r, 0, H, W)
            if s1 >= mid and s2 >= mid:
                return True
        # vertical cuts
        for c in range(1, W):
            s1 = rect_sum(0, 0, H, c)
            s2 = rect_sum(0, c, H, W)
            if s1 >= mid and s2 >= mid:
                return True
        return False

    # For N=3:
    # Try horizontal cuts into 3 parts
    for r1 in range(1, H):
        for r2 in range(r1+1, H):
            sums = [rect_sum(0, 0, r1, W), rect_sum(r1, 0, r2, W), rect_sum(r2, 0, H, W)]
            if min(sums) >= mid:
                return True
    # vertical cuts into 3 parts
    for c1 in range(1, W):
        for c2 in range(c1+1, W):
            sums = [rect_sum(0, 0, H, c1), rect_sum(0, c1, H, c2), rect_sum(0, c2, H, W)]
            if min(sums) >= mid:
                return True
    # 1 horizontal + 1 vertical cut = 4 rectangles, select any 3 with sums >= mid
    for r in range(1, H):
        for c in range(1, W):
            rects = [
                rect_sum(0, 0, r, c),
                rect_sum(0, c, r, W),
                rect_sum(r, 0, H, c),
                rect_sum(r, c, H, W)
            ]
            # Choose any 3 rectangles with sums >= mid
            # Because who does not get land is allowed, so we assign to 3 brothers the 3 rectangles with largest sums >= mid
            rects = sorted(rects, reverse=True)
            if rects[2] >= mid:  # the third largest is >= mid means at least 3 rectangles >= mid
                return True
    return False

    # For N=4:
    # Try 2 horizontal and 1 vertical cut to get 6 rectangles, pick 4 with sums >= mid?
    # This seems complex, instead:
    # Try 1 horizontal + 1 vertical cut = 4 rectangles
    # We want all 4 with sum >= mid
    # So iterate all pairs of cuts
def can4(mid):
    for r in range(1, H):
        for c in range(1, W):
            rects = [
                rect_sum(0, 0, r, c),
                rect_sum(0, c, r, W),
                rect_sum(r, 0, H, c),
                rect_sum(r, c, H, W)
            ]
            if min(rects) >= mid:
                return True
    # Try 3 horizontal cuts to create 4 rectangles vertically combined
    for r1 in range(1, H):
        for r2 in range(r1+1, H):
            for r3 in range(r2+1, H):
                sums = [
                    rect_sum(0, 0, r1, W),
                    rect_sum(r1, 0, r2, W),
                    rect_sum(r2, 0, r3, W),
                    rect_sum(r3, 0, H, W)
                ]
                if min(sums) >= mid:
                    return True
    # Try 3 vertical cuts to create 4 rectangles horizontally combined
    for c1 in range(1, W):
        for c2 in range(c1+1, W):
            for c3 in range(c2+1, W):
                sums = [
                    rect_sum(0, 0, H, c1),
                    rect_sum(0, c1, H, c2),
                    rect_sum(0, c2, H, c3),
                    rect_sum(0, c3, H, W)
                ]
                if min(sums) >= mid:
                    return True
    return False

lo, hi = 0, 10**9
while lo < hi:
    mid = (lo + hi + 1) // 2
    if N == 4:
        if can4(mid):
            lo = mid
        else:
            hi = mid - 1
    else:
        if can(N, mid):
            lo = mid
        else:
            hi = mid - 1

print(lo)