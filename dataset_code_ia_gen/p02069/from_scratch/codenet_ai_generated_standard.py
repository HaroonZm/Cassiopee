import sys
input = sys.stdin.readline

N,L = map(int,input().split())
intervals = [tuple(map(int,input().split())) for _ in range(N)]

# Compute x: minimum intervals to cover [0,L)
intervals.sort(key=lambda x: (x[0], -x[1]))
res = 0
end = 0
i = 0
while end < L:
    far = end
    while i < N and intervals[i][0] <= end:
        if intervals[i][1] > far:
            far = intervals[i][1]
        i += 1
    if far == end:
        # no extension possible, but problem states union covers [0,L), so no gap
        break
    end = far
    res += 1
x = res

# Compute y: minimum number y so that any y intervals cover [0,L)
# Equivalent to the size of minimal subset whose removal breaks coverage
# So, y = N - max number of intervals can be removed while still covering [0,L)
# But to find max number of intervals that can be removed while still covering [0,L)
# is complex; use a line sweep to find maximum overlap minimum cover size

# Idea: y = minimal number of intervals needed to always cover [0,L),
# i.e. minimal number s.t. any combination of that size covers [0,L)
# Complement: if removing k intervals breaks coverage, then y ≤ N-k

# So find the maximal number of intervals that can be removed (k)
# so that coverage is broken. Then y = N-k

# Approach: find minimal interval cover (as x), any set of intervals missing one interval in the cover breaks [0,L)
# However, x ≤ y ≤ N

# To find y:
# For each point in [0,L), count how many intervals cover it; minimal coverage count over [0,L) is min_coverage
# Then y = min_coverage

# Because if we choose less than min_coverage intervals, it's possible to avoid fully covering [0,L)
# To compute minimal coverage over [0,L):

events = []
for l,r in intervals:
    events.append((l,1))
    events.append((r,-1))
events.sort()

cov = 0
min_cov = 10**9
prev = 0
for pos,typ in events:
    if pos > prev and cov < min_cov:
        min_cov = cov
    cov += typ
    prev = pos
if prev < L and cov < min_cov:
    min_cov = cov
y = min_cov

print(x,y)