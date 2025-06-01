N,M=map(int,input().split())
A=[]
for i in range(N):
  A.append(int(input()))
for i in range(M):
  for j in range(N-1):
    if A[j]%(i+1)>A[j+1]%(i+1):
      X=A[j]
      A[j]=A[j+1]
      A[j+1]=X
for i in range(N):
  print(A[i])