n,m = map(int,input().split())
t = [[0]*(n+2) for i in range(n+2)]

for i in range(m):
    a,b,x = map(int,input().split())
    a -= 1
    b -= 1
    t[a][b] += 1
    t[a][b+1] -= 1
    t[a+x+1][b] -= 1
    t[a+x+1][b+x+2] += 1
    t[a+x+2][b+1] += 1
    t[a+x+2][b+x+2] -= 1
    
for i in range(n+2):
    for j in range(1,n+2):
        t[i][j] += t[i][j-1]
        
for i in range(n+2):
    for j in range(1,n+2):
        t[j][i] += t[j-1][i]
    
for i in range(1, n+2):
    for j in range(1,n+2):
        t[i][j] += t[i-1][j-1]
        
ans = 0
for i in range(n):
    for j in range(i+1):
        if t[i][j] != 0:
            ans += 1
            
print(ans)