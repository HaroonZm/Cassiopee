N, Z, W = map(int, raw_input().split())
A = map(int, raw_input().split())
if N == 1:
  print abs(W-A[-1])
else:
  print max(abs(W-A[-1]), abs(A[-1]-A[-2]))