n,m = map(int, input().split())
a = list(map(int, [input() for _ in range(n)]))

ranges = []
for _ in range(m):
    l,r = map(int, input().split())
    ranges.append((l, r))

# solution idea:
# Because if any two selected trees are covered together by any interval,
# we can't pick both. So each interval forbids selecting 2 or more trees inside it.
# This means that the set of selected trees must be an independent set
# in the interval overlap graph.
#
# A simple solution (not optimized) is to:
# - Sort intervals by their right endpoint
# - For each interval, we cannot select 2 or more trees inside it
# - So only one tree per interval can be selected.
# Because intervals can overlap arbitrarily, to satisfy all constraints,
# if two trees lie in any forbidden interval together, only one can be chosen.
#
# We'll select trees greedily from left to right,
# skipping trees that would violate any forbidden interval.
#
# Since the problem is complex and large constraints,
# and we need a simple approach for a beginner,
# we'll implement the following:
# For each tree from left to right, we'll check if selecting it causes conflict.
# A conflict happens if:
# - For any interval covering this tree, already one tree inside that interval is selected.
# We'll keep track, for each interval, if a tree is selected inside it.
#
# We'll have a list to record if a tree is selected.
# For each tree i:
#   For all intervals covering i:
#       if already selected a tree inside that interval, skip current tree
# If no conflict for all intervals containing i, select tree i and mark intervals accordingly.
#
# Because M and N can be large, this naive approach will be slow,
# but it's good for beginner level and correctness.

selected = [False]*n

# For each tree, which intervals cover it?
# Build list of intervals for each tree
cover_intervals = [[] for _ in range(n)]
for idx, (l,r) in enumerate(ranges):
    for i in range(l-1, r):
        cover_intervals[i].append(idx)

# For each interval, keep track if a tree inside it is already selected
interval_selected = [False]*m

res = 0
for i in range(n):
    conflict = False
    for interval_idx in cover_intervals[i]:
        if interval_selected[interval_idx]:
            conflict = True
            break
    if not conflict:
        selected[i] = True
        res += a[i]
        for interval_idx in cover_intervals[i]:
            interval_selected[interval_idx] = True

print(res)