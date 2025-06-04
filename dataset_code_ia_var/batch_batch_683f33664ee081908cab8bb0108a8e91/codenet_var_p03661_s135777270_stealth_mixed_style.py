n = int(input())
A = [int(x) for x in input().split()]
def accum(l):  # mix imperative and functional
  res = []
  s = 0
  for e in l:
    s += e
    res.append(s)
  return res
A = accum(A)
from functools import reduce
answer = 10**12
i = 0
while i < n-1:
    xi = A[i]
    yi = A[-1] - xi
    answer = min(answer, abs(xi-yi))
    i += 1
print(answer)