N, M = map(int, input().split())
S = [[int(i) for i in input().split()] for j in range(M)]
p = [int(i) for i in input().split()]
ans = 0
#print(S)
for i in range(2 ** N):
  T = [0] * N
  for j in range(N):
    if ((i >> j) & 1):
      T[j] += 1

  s = 0
  for j in range(M):
    pp = 0
    for k in range(S[j][0]):
      pp += T[S[j][k+1]-1]
    if pp % 2 == p[j]:
      s += 1
      #print(pp, p[j])
  if s == M:
    #print(T)
    ans += 1
print(ans)