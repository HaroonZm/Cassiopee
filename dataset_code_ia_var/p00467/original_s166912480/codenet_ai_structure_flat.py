for e in iter(input, '0 0'):
 N, M = map(int, e.split())
 S = []
 for _ in range(N):
  S.append(int(input()))
 p = 1
 b = 1
 i = 0
 while i < M:
  d = int(input())
  p = p + d
  if N <= p:
   if b:
    print(i + 1)
    b = 0
   i = i + 1
   continue
  p = p + S[p - 2]
  if N <= p and b:
   print(i + 1)
   b = 0
  i = i + 1