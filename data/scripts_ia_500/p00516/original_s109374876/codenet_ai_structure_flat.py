N,M=map(int,input().split())
A=[]
for _ in range(N):
    A.append(int(input()))
B=[]
for _ in range(M):
    B.append(int(input()))
C=[0]*N
for j in range(M):
    b=B[j]
    for i in range(N):
        if A[i]<=b:
            C[i]+=1
            break
c=0
index=0
for i in range(N):
    if C[i]>c:
        c=C[i]
        index=i
print(index+1)