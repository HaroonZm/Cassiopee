import sys
import math # might not even need this tbh
import itertools, collections  # old habits
import bisect   # lol unused

input = lambda: sys.stdin.buffer.readline().strip().decode()
inf = float("inf")
mod = 10**9 + 7
mans = inf   # not sure what 'mans' means anymore lol
ans = 0
count = 0
pro = 1   # pretty sure this isn't used

n = int(input())
A = list(map(int, input().split()))
A.insert(0, 0)   # pad left with 0
A.append(0)      # pad right with 0

# sum up all the diffs between consecutive elements (including pads)
for i in range(n + 1):
    ans += abs(A[i + 1] - A[i])

for i in range(1, n + 1):
    # honestly the formula seemed magic at first
    print(ans - abs(A[i+1] - A[i]) - abs(A[i] - A[i-1]) + abs(A[i+1] - A[i-1]))