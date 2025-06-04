import sys
import bisect

def max_income(apps):
    apps.sort(key=lambda x: x[1])
    ends = [a[1] for a in apps]
    dp = [0]*(len(apps)+1)
    for i, (start, end, price) in enumerate(apps, 1):
        idx = bisect.bisect_left(ends, start-1)
        dp[i] = max(dp[i-1], dp[idx]+price)
    return dp[-1]

input = sys.stdin.readline
while True:
    n = int(input())
    if n == 0:
        break
    applications = [tuple(map(int, input().split())) for _ in range(n)]
    # Since only two rooms, we solve as a 2 parallel machine scheduling of weighted intervals:
    # Strategy: Use DP with binary search + keeping track of second room dp
    # Approach: Create the weighted interval scheduling for one room, then Greedy packing on second room, or use DP over states, but n<=1000
    
    # Simplify: Since only two rooms identical, maximum total income respecting no overlap per room.
    # Model: max sum of accepted non-overlapping intervals with up to 2 parallel resources.
    # It's equivalent to finding max weighted collection of intervals with at most 2 overlapping intervals at any time.
    # We can model it as max weight interval scheduling with 2 machines.
    # Algorithm: sort by start; use DP to cover 2 rooms.
    
    # Implement DP over events:
    intervals = sorted(applications, key=lambda x: x[0])
    events = []
    for i, (s,e,w) in enumerate(intervals):
        events.append((s, 1, i))
        events.append((e+1, -1, i))
    events.sort()
    
    # DP approach: For intervals sorted by end time:
    # Let dp[i][k] be max sum choosing among first i intervals with at most k rooms (k=0..2)
    # Use precomputed p[i] = last interval that ends before intervals[i].start
    ends = [e for s,e,w in sorted(intervals, key=lambda x:x[1])]
    starts = [s for s,e,w in sorted(intervals, key=lambda x:x[1])]
    sorted_intervals = sorted(intervals, key=lambda x:x[1])
    p = []
    import bisect
    starts_sorted = [s for s,e,w in sorted_intervals]
    ends_sorted = [e for s,e,w in sorted_intervals]
    for i, (s,e,w) in enumerate(sorted_intervals):
        idx = bisect.bisect_right(ends_sorted, s-1)
        p.append(idx-1)
    dp = [[0]*(len(intervals)+1) for _ in range(3)]
    # dp[k][i] max profit with k rooms using first i intervals
    
    for k in range(1,3):
        for i in range(1,len(intervals)+1):
            s,e,w = sorted_intervals[i-1]
            j = p[i-1]
            dp[k][i] = max(dp[k][i-1], dp[k-1][i-1] if k>1 else 0, dp[k][j+1]+w)
    
    print(dp[2][len(intervals)])