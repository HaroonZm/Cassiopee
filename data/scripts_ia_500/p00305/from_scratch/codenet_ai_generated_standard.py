N=int(input())
p=[list(map(int,input().split())) for _ in range(N)]
S=[[0]*(N+1) for _ in range(N+1)]
for i in range(N):
    for j in range(N):
        S[i+1][j+1]=S[i+1][j]+p[i][j]
max_sum=-10**9
for r1 in range(N):
    for r2 in range(r1,N):
        row_top=p[r1]
        row_bot=p[r2]
        arr=[]
        for c in range(N):
            if r1==r2:
                arr.append(p[r1][c])
            else:
                arr.append(row_top[c]+row_bot[c])
        ps=[0]
        for val in arr:
            ps.append(ps[-1]+val)
        for c1 in range(N):
            for c2 in range(c1,N):
                if r1!=r2 and c2-c1>0:
                    mid_sum=0
                    for rr in range(r1+1,r2):
                        mid_sum+=p[rr][c1]+p[rr][c2]
                    total=ps[c2+1]-ps[c1]+mid_sum
                else:
                    total=ps[c2+1]-ps[c1]
                if total>max_sum:
                    max_sum=total
print(max_sum)