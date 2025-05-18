N,X,Y=map(int,input().split())

C=[0]*N
for i in range(1,N):
  for j in range(i+1,N+1):
    C[min(j-i,abs(X-i)+1+abs(j-Y),abs(Y-i)+1+abs(j-X))]+=1

for i in range(1,N):
  print(C[i])