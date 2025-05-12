def insertR(a, b):
  if a not in R: R[a] = {}
  if b not in R[a]: R[a][b] = 0

N = int(input())
A = list(map(int, input().split()))

if N == 1:
  print(1)
  exit()

DP = [[-1] * (N + 1) for _ in range(N + 1)]
D = [-1] * (N + 1)
R = {}
for i in range(5):
  a = A[i]
  if a in R:
    R[a] += 1
  else:
    R[a] = 1

Flag = 0
for i in R.keys():
  if R[i] >= 3:
    Flag = 1
    R[i] -= 3

L = []
for i in R.keys():
  if R[i] == 2:
    L.append(i)
    DP[i][i] = Flag
    D[i] = Flag
  elif R[i] == 1:
    L.append(i)
    D[i] = Flag

for i in range(len(L) - 1):
  for j in range(i + 1, len(L)):
    DP[L[i]][L[j]] = Flag

common = 0
for i in range(5, N * 3 - 3, 3):
  L = []
  for j in range(i, i + 3):
    for k in range(len(L)):
      if L[k][1] == A[j]:
        L[k][0] += 1
        break
    else :
      L.append([1, A[j]])
  L.sort()
  R = {}
  # 3
  if len(L) == 1:
    common += 1
  # 1:2
  elif len(L) == 2:
    a = L[0][1]
    b = L[1][1]
    # 1個のほうを揃える場合
    if DP[a][a] != -1:
      insertR(b, b)
      R[b][b] = max([R[b][b], DP[b][b], DP[a][a] + 1])
    # 2個のほうを揃える場合
    for j in range(N + 1):
      n = max(DP[b][j], DP[j][b])
      if n == -1: continue
      insertR(a, j)
      R[a][j] = max([R[a][j], DP[a][j], n + 1])
    # 揃えない場合
    for j in range(N + 1):
      n = D[j]
      if n == -1: continue
      insertR(a, j)
      R[a][j] = max(R[a][j], n)
      insertR(b, j)
      R[b][j] = max(R[b][j], n)
    n = max(D)
    insertR(a, b)
    R[a][b] = max(R[a][b], n)
    insertR(b, b)
    R[b][b] = max(R[b][b], n)
  # 1:1:1
  elif len(L) == 3:
    a = L[0][1]
    b = L[1][1]
    c = L[2][1]
    insertR(b, c)
    insertR(a, c)
    insertR(a, b)
    #揃える場合
    if DP[a][a] != -1:  
      R[b][c] = max(R[b][c], DP[a][a] + 1)
    if DP[b][b] != -1:      
      R[a][c] = max(R[a][c], DP[b][b] + 1)
    if DP[c][c] != -1:
      R[a][b] = max(R[a][b], DP[c][c] + 1)
    #揃えない場合
    for j in range(N + 1):
      n = D[j]
      if n == -1: continue
      insertR(a, j)
      R[a][j] = max(R[a][j], n)
      insertR(b, j)
      R[b][j] = max(R[b][j], n)
      insertR(c, j)
      R[c][j] = max(R[c][j], n)
    n = max(D)
    R[a][b] = max(R[a][b], n)
    R[b][c] = max(R[b][c], n)
    R[a][c] = max(R[a][c], n)

  for k in R.keys():
    for kk in R[k].keys():
      n = R[k][kk]
      DP[k][kk] = max(DP[k][kk], n)
      DP[kk][k] = max(DP[kk][k], n)
      D[k] = max(D[k], n)
      D[kk] = max(D[kk], n)

a = A[-1]
if DP[a][a] != -1:
  DP[a][a] += 1

ans = 0
for i in DP:
  for j in i:
    ans = max(ans, j)

ans += common

print(ans)