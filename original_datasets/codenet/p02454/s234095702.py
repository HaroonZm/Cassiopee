import sys
import bisect
input()
arr = list(map(int, input().split()))
nq = int(input())
lines = sys.stdin.readlines()
ans = [None] * nq
for i in range(nq):
    q = int(lines[i])
    ans[i] = '{} {}'.format((bisect.bisect_left(arr, q)), bisect.bisect_right(arr, q))
print('\n'.join(ans))