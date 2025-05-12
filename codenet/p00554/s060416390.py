N,M=map(int,input().split())
AB=list()
for i in range(M):
  AB.append(list(map(int,input().split())))
C=0
AB.sort(reverse=True)
for i in range(M-1):
  C=C+max(0,N-AB[i][0])
print(C)