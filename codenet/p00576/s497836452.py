N=int(input())
X=list(map(int,input().split()))
M=int(input())
A=list(map(int,input().split()))
A=[A[i]-1 for i in range(len(A))]

for i in range(M):
    l=A[i]
    if X[l]+1 not in X and X[l]!=2019:
        X[l]+=1
print(format("\n".join(map(str,X))))