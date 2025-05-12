from collections import deque

N, M = map(int, input().split())
ab = [[] for i in range(N)]
for _ in range(M) :
  a, b = map(int, input().split())
  ab[a-1].append(b-1)
  ab[b-1].append(a-1)
Q = int(input())
vdc = [[int(i) for i in input().split()] for _ in range(Q)]

C = [0] * N
D = [-1] * N
for v, d, c in vdc[::-1] :
  q = deque([(v - 1, d, c)])
  while q :
    cv, cd, cc = q.popleft()
    if D[cv] >= cd :
      continue
    D[cv] = cd
    if C[cv] == 0 :
      C[cv] = cc
    for nv in ab[cv] :
      q.append((nv, cd - 1, cc))

for i in range(N) :
  print(C[i])