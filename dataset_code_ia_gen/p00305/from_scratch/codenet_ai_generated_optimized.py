n=int(input())
p=[list(map(int,input().split())) for _ in range(n)]
s=[[0]*(n+1) for _ in range(n+1)]
for i in range(n):
    for j in range(n):
        s[i+1][j+1]=s[i+1][j]+p[i][j]
max_sum=float('-inf')
for r1 in range(n):
    for r2 in range(r1,n):
        arr=[s[r2+1][j+1]-s[r1][j+1] for j in range(n)]
        prefix=[0]
        for v in arr:
            prefix.append(prefix[-1]+v)
        for c1 in range(n):
            for c2 in range(c1,n):
                width=c2-c1+1
                height=r2-r1+1
                if width<=2 or height<=2:
                    total=prefix[c2+1]-prefix[c1]
                else:
                    inner=prefix[c2]-prefix[c1+1]
                    border=prefix[c2+1]-prefix[c1]-inner
                    total=border
                if total>max_sum:
                    max_sum=total
print(max_sum)