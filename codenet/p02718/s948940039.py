N, M = map(int, input().split())
A = list(map(int, input().split()))
S = sum(A)
c = sum(1 for a in A if a*4*M >= S)
if c >= M:
  print("Yes")
else:
  print("No")