n,k=map(int,input().split())
A=list(map(int,input().split()))
for i in range(1, n-k+1):
    print("Yes" if A[i+k-1]>A[i-1] else "No")