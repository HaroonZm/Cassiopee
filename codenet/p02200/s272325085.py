N=int(input())
A=list(map(int,input().split()))
result=0

for i in range(1,N):
    if A[i]>A[i-1]:
        result+=1

print(result)