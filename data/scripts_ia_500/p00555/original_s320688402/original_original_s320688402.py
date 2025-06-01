n,m,d=map(int,input().split())
mp=[input() for _ in range(n)]
t='.'*d
cnt=0
for i in range(n):
    for j in range(m):
        if j<=m-d and mp[i][j:j+d]==t:
            cnt+=1
        if i<=n-d:
            ns=''
            for l in range(d):
                ns+=mp[i+l][j]
                if ns==t:
                    cnt+=1
print(cnt)