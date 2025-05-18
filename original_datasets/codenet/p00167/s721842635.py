while True:
  N, M, C = input(), [], 0
  if not N:
    break
  for i in range(N):
    M.append(input())
  for p in range(N)[::-1]:
    for i in range(p):
      if M[i] > M[i + 1]:
        M[i], M[i + 1] = M[i + 1], M[i]
        C += 1
  print(C)