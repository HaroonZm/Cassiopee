import sys
input = sys.stdin.readline

N = int(input())
points = [tuple(map(int, input().split())) for _ in range(N)]

# Manhattan distance: |x - x'| + |y - y'|
# Let's consider the transformation:
# d1 = x + y
# d2 = x - y
# For points of same theme, max distance ≤ M means difference in d1 ≤ M and difference in d2 ≤ M

d1 = [x + y for x, y in points]
d2 = [x - y for x, y in points]

max_d1 = max(d1)
min_d1 = min(d1)
max_d2 = max(d2)
min_d2 = min(d2)

# If we put all points in one theme, max distance is max(max_d1 - min_d1, max_d2 - min_d2)
# But the problem says we cannot assign all points same theme.
# So we must split into two themes.

# Since the themes partition points, the maximum distance M is at least half the total spread
# in one of the transformed coordinates because dividing points into two groups can't
# reduce the maximum distance below that.

# We'll try to split points by comparing median values and find minimal max intra-theme distance.

# A simple approach:
# binary search on M
# for a given M, check if we can split points into two groups so that in each group,
# max distance ≤ M.

def can_split(M):
    # Try to split by d1 or d2
    # For both d1 and d2, try to assign points to group 1 or 2 such that
    # points in each group have d1 or d2 values within M.

    # We'll try to split by d1:
    d1_sorted = sorted(d1)
    # group1: points with d1 <= some value, group2: others
    for i in range(N-1):
        # check range in group1 and group2
        g1_min = d1_sorted[0]
        g1_max = d1_sorted[i]
        g2_min = d1_sorted[i+1]
        g2_max = d1_sorted[-1]
        if g1_max - g1_min <= M and g2_max - g2_min <= M:
            return True

    # try split by d2:
    d2_sorted = sorted(d2)
    for i in range(N -1):
        g1_min = d2_sorted[0]
        g1_max = d2_sorted[i]
        g2_min = d2_sorted[i+1]
        g2_max = d2_sorted[-1]
        if g1_max - g1_min <= M and g2_max - g2_min <= M:
            return True

    return False

low = 0
high = max(max_d1 - min_d1, max_d2 - min_d2)

while low < high:
    mid = (low + high) // 2
    if can_split(mid):
        high = mid
    else:
        low = mid +1

print(low)