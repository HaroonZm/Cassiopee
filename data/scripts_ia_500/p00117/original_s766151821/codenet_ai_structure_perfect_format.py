n=int(input())
m=int(input())
K=[[10**9 for _ in range(32)] for _ in range(32)]
for _ in range(m):
    a,b,c,d=map(int,input().split(","))
    K[a][b]=c
    K[b][a]=d
for k in range(1,n+1):
    for j in range(1,n+1):
        for i in range(1,n+1):
            if K[i][j]>K[i][k]+K[k][j]:
                K[i][j]=K[i][k]+K[k][j]
s,g,V,P=map(int,input().split(","))
print(V-P-K[s][g]-K[g][s])