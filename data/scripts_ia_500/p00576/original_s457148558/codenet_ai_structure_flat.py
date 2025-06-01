N=int(input())
X=list(map(int,input().split()))
M=int(input())
A=list(map(int,input().split()))
for i in A:
    if not ((X[i-1]+1) in X or X[i-1]==2019):
        X[i-1]+=1
for i in range(N):
    print(X[i])