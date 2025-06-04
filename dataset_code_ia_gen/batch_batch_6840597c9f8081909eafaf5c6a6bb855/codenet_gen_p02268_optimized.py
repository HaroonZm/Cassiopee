import sys
import bisect

input = sys.stdin.readline
n = int(input())
S = list(map(int, input().split()))
q = int(input())
T = list(map(int, input().split()))

count = 0
for t in T:
    i = bisect.bisect_left(S, t)
    if i != n and S[i] == t:
        count += 1

print(count)