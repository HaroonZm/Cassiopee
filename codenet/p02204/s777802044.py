M, N = map(int, input().split())
A = [int(i) for i in input().split()]

if M == 2 :
  a, b = 0, 0
  for i in range(N) :
    if (i % 2) == (A[i] % 2) :
      a += 1
    else :
      b += 1
  print(min(a, b))
  
else :
  ret = 0
  for i in range(1, N) :
    if A[i] == A[i - 1] :
      ret += 1
      A[i] = 0
      
  print(ret)