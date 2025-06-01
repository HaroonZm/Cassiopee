N=int(input())
X=list(map(int,input().split()))
M=int(input())
A=list(map(int,input().split()))
for i in range(len(A)):
    A[i]-=1
for i in range(M):
    l=A[i]
    if X[l]!=2019:
        incremented=X[l]+1
        found=False
        for val in X:
            if val==incremented:
                found=True
                break
        if not found:
            X[l]=incremented
for val in X:
    print(val)