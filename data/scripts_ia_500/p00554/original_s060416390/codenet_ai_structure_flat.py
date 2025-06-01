N,M=map(int,input().split())
AB=[]
for _ in range(M):
    AB.append(list(map(int,input().split())))
AB.sort(reverse=True)
C=0
for i in range(M-1):
    if N-AB[i][0]>0:
        C+=N-AB[i][0]
print(C)