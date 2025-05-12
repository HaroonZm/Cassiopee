import sys
input = sys.stdin.readline
from collections import Counter

n = int(input())
A = sorted(map(int, input().split()), reverse=True)
C = Counter(A)
ans = 0
for a in A:
  if not C[a]:
    continue
  r = (1<<a.bit_length()) - a
  if r != a:
    if r in C and C[r] > 0:
      ans += 1
      C[r] -= 1
  else:
    if C[r] >= 2:
      ans += 1
      C[r] -= 1
  C[a] -= 1
print(ans)