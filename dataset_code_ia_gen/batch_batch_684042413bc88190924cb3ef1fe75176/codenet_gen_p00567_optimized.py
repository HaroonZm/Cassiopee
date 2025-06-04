N=int(input())
L=[int(input()) for _ in range(N)]
A=[0]*(N+1)
for i in range(N):
    A[i+1]=A[i]+L[i]
ans=float('inf')
for i in range(N):
    for j in range(i+1,N+1):
        pieces=[A[k]-A[k-1] for k in range(i+1,j+1)]
        if len(pieces)>1:
            diff=max(pieces)-min(pieces)
            if diff<ans:
                ans=diff
print(ans)