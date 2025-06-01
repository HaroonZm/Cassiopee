n,m = map(int,input().split())
t = [[0]*(n+2) for _ in range(n+2)]
for _ in range(m):
    a,b,x = map(int,input().split())
    a -= 1
    b -= 1
    t[a][b] += 1
    t[a][b+1] -= 1
    t[a+x+1][b] -= 1
    t[a+x+1][b+x+2] += 1
    t[a+x+2][b+1] += 1
    t[a+x+2][b+x+2] -= 1
i=0
while i<n+2:
    j=1
    while j<n+2:
        t[i][j] += t[i][j-1]
        j+=1
    i+=1
i=0
while i<n+2:
    j=1
    while j<n+2:
        t[j][i] += t[j-1][i]
        j+=1
    i+=1
i=1
while i<n+2:
    j=1
    while j<n+2:
        t[i][j] += t[i-1][j-1]
        j+=1
    i+=1
ans=0
i=0
while i<n:
    j=0
    while j<=i:
        if t[i][j]!=0:
            ans+=1
        j+=1
    i+=1
print(ans)