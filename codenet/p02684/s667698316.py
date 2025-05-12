import sys
readline = sys.stdin.readline

N,K = map(int,readline().split())
A = [0] + list(map(int,readline().split()))
now = 1

while K:
  if K & 1:
    now = A[now]
  nex = [0] * (N + 1)
  for i in range(N + 1):
    nex[i] = A[A[i]]
  A = nex
  K >>= 1
  
print(now)