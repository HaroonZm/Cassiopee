#B
N = int(input())
A = []
B = []
C = []

for i in range(N):
    a,b,c = map(int,input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    
ans = [0]*N
for i in range(N):
    a,b,c = A[i],B[i],C[i]
    if A.count(a) == 1:
        ans[i]+=a
    if B.count(b) == 1:
        ans[i]+=b
    if C.count(c) == 1:
        ans[i]+=c
        
    print(ans[i])