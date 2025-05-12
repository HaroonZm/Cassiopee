K,N = map(int,input().split())
A = list(map(int,input().split()))
B =[]
for i in range(N-1):
  B.append(A[i+1]-A[i])
B.append(A[0]+K-A[N-1])
print(K-max(B))