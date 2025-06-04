import sys
import bisect

input = sys.stdin.readline

N, Q = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

for _ in range(Q):
    l, r = map(int, input().split())
    left_idx = bisect.bisect_left(a, l)
    right_idx = bisect.bisect_right(a, r)
    print(right_idx - left_idx)