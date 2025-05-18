def swap(i,j):
  X=A[i]
  A[i]=A[j]
  A[j]=X

N,M=map(int,input().split())
A=list()
for i in range(N):
  A.append(int(input()))
for i in range(M):
  for j in range(N-1):
    if A[j]%(i+1)>A[j+1]%(i+1):
      swap(j,j+1)
for i in range(N):
  print(A[i])