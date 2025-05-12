N, M ,X = map(int, input().split())
A = list(map(int, input().split()))

import bisect

idx = bisect.bisect_right(A, X)

print(min(len(A[:idx]), len(A[idx:])))