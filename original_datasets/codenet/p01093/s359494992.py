while 1:
  n = int(input())
  if n == 0:
    break
  A = list(map(int, input().split()))
  A.sort()
  m = 1000000
  t=0
  for i in range(n):
    for j in range(1+i,n):
      t=abs(A[i]-A[j])
      if t<= m:
        m = t
  print(m)