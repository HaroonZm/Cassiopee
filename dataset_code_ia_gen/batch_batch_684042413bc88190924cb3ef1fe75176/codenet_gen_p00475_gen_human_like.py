import sys
input = sys.stdin.readline

N = int(input())
points = [tuple(map(int, input().split())) for _ in range(N)]

# Transform coordinates to u,v where u = x+y, v = x-y
u = [x + y for x, y in points]
v = [x - y for x, y in points]

INF = 10**15

# Define a function to compute max distance between points in one group
def max_dist(arr):
    return max(arr) - min(arr)

# Since themes partition the set into two non-empty subsets,
# and the cost is Manhattan distance,
# the minimal maximum distance M is min over all partitions (except all same theme) of max distance in theme groups.
# Trying all partitions is impossible. But since Manhattan distance = max(|u1-u2|, |v1-v2|),
# the maximum distance within a group is at least half of max delta in u or v coordinates.

# The idea is to split points by a line in (u,v) space:
# Sorting points by u or v, trying to split them into two groups,
# and compute max distance in each group (for both u and v dimensions),
# then take minimal maximum distance over all splits.

# We'll try sorting points by u and v separately, and split at every position,
# then find the minimum possible max distance in groups.

# Make a list of (u,v) and sort by u
points_uv = list(zip(u,v))

points_uv.sort()
prefix_min_v = [INF]*(N+1)
prefix_max_v = [-INF]*(N+1)
suffix_min_v = [INF]*(N+1)
suffix_max_v = [-INF]*(N+1)

prefix_min_u = [INF]*(N+1)
prefix_max_u = [-INF]*(N+1)
suffix_min_u = [INF]*(N+1)
suffix_max_u = [-INF]*(N+1)

for i in range(N):
    ui, vi = points_uv[i]
    prefix_min_v[i+1] = min(prefix_min_v[i], vi)
    prefix_max_v[i+1] = max(prefix_max_v[i], vi)
    prefix_min_u[i+1] = min(prefix_min_u[i], ui)
    prefix_max_u[i+1] = max(prefix_max_u[i], ui)

for i in range(N-1, -1, -1):
    ui, vi = points_uv[i]
    suffix_min_v[i] = min(suffix_min_v[i+1], vi)
    suffix_max_v[i] = max(suffix_max_v[i+1], vi)
    suffix_min_u[i] = min(suffix_min_u[i+1], ui)
    suffix_max_u[i] = max(suffix_max_u[i+1], ui)

ans = INF
for i in range(1, N):  # split into [0..i-1] and [i..N-1], both non-empty
    # group1 max delta_u and delta_v
    delta_u1 = prefix_max_u[i] - prefix_min_u[i]
    delta_v1 = prefix_max_v[i] - prefix_min_v[i]
    max1 = max(delta_u1, delta_v1)
    # group2 max delta_u and delta_v
    delta_u2 = suffix_max_u[i] - suffix_min_u[i]
    delta_v2 = suffix_max_v[i] - suffix_min_v[i]
    max2 = max(delta_u2, delta_v2)

    cur = max(max1, max2)
    ans = min(ans, cur)

# Repeat the process sorting by v

points_uv.sort(key=lambda x: x[1])

prefix_min_u = [INF]*(N+1)
prefix_max_u = [-INF]*(N+1)
suffix_min_u = [INF]*(N+1)
suffix_max_u = [-INF]*(N+1)

prefix_min_v = [INF]*(N+1)
prefix_max_v = [-INF]*(N+1)
suffix_min_v = [INF]*(N+1)
suffix_max_v = [-INF]*(N+1)

for i in range(N):
    ui, vi = points_uv[i]
    prefix_min_u[i+1] = min(prefix_min_u[i], ui)
    prefix_max_u[i+1] = max(prefix_max_u[i], ui)
    prefix_min_v[i+1] = min(prefix_min_v[i], vi)
    prefix_max_v[i+1] = max(prefix_max_v[i], vi)

for i in range(N-1, -1, -1):
    ui, vi = points_uv[i]
    suffix_min_u[i] = min(suffix_min_u[i+1], ui)
    suffix_max_u[i] = max(suffix_max_u[i+1], ui)
    suffix_min_v[i] = min(suffix_min_v[i+1], vi)
    suffix_max_v[i] = max(suffix_max_v[i+1], vi)

for i in range(1, N):
    delta_u1 = prefix_max_u[i] - prefix_min_u[i]
    delta_v1 = prefix_max_v[i] - prefix_min_v[i]
    max1 = max(delta_u1, delta_v1)

    delta_u2 = suffix_max_u[i] - suffix_min_u[i]
    delta_v2 = suffix_max_v[i] - suffix_min_v[i]
    max2 = max(delta_u2, delta_v2)

    cur = max(max1, max2)
    ans = min(ans, cur)

# If all points assigned same theme, then max distance = max delta_u or delta_v for all points
# But problem states not all same theme
# So answer is ans

print(ans)