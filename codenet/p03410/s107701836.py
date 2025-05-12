import numpy as np
n = int(input())
A = np.array(list(map(int, input().split())), dtype=np.int64)
B = np.array(list(map(int, input().split())), dtype=np.int64)
ans = 0
for i in range(30):
  t = 1<<i
  C = B.copy()%(2*t)
  E = A.copy()%(2*t)
  C.sort()
  E.sort()
  D = np.searchsorted(C, 2*t-E, side="left")
  D -= np.searchsorted(C, t-E, side="left")
  D += np.searchsorted(C, 4*t-E, side="left")
  D -= np.searchsorted(C, 3*t-E, side="left")
  cnt = D.sum()%2
  ans |= cnt << i
print(ans)