x,y=map(int,input().split())
A=list(list(map(int,input().split())) for i in range(x))
B=list(int(input()) for i in range(y))
ans=[]
for i in range(x):
    count=0
    for j in range(y):
        count +=A[i][j]*B[j]
    ans.append(count)
for i in range(len(ans)):print(ans[i])