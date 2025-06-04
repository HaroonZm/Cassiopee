N=int(input())
A=list(map(int,input().split()))
ANS=1
for i in range(1,N):
    if A[i]<=A[i-1]:
        ANS+=1
print(ANS)
print(N)