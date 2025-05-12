#B問題
N,M = map(int,input().split())
A = [int(input()) for i in range(N)]
B = [int(input()) for j in range(M)]
C = [0 for i in range(N)]
for j in range(M):
    b = B[j]
    for i in range(N):
        if A[i] <= b:
            C[i]+=1
            break
            
c = max(C)
print(C.index(c)+1)