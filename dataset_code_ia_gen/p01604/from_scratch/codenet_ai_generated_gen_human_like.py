N = int(input())
lines = [input() for _ in range(N)]

label_to_index = {}
for i, line in enumerate(lines):
    if line.endswith(':'):
        label = line[:-1]
        label_to_index[label] = i

# Build next line index for each line
next_indices = [None] * N
for i in range(N):
    line = lines[i]
    if line.endswith(':'):
        # label line, next line is i+1 if exists
        next_indices[i] = i + 1 if i + 1 < N else N
    else:
        # goto line: extract label and jump to that label line
        label = line[5:-1] # "goto LABEL;" => LABEL
        next_indices[i] = label_to_index[label]

# We'll compute minimal number of goto removals to reach end from line i
# If line i is beyond N-1 (i == N), we are finished and cost is 0
# For each goto line, we have two choices:
#  - remove goto (stop here and terminate): cost = 1
#  - keep goto: cost = dp[next_index]
# For label lines, cost = dp[next_index]

from functools import lru_cache

@lru_cache(None)
def dp(i):
    if i == N:
        return 0
    # If label line
    if lines[i].endswith(':'):
        return dp(next_indices[i])
    else:
        # goto line
        # option 1: remove goto, terminate here with 1 removal
        cost_remove = 1
        # option 2: keep goto and continue
        cost_keep = dp(next_indices[i])
        return min(cost_remove, cost_keep)

print(dp(0))