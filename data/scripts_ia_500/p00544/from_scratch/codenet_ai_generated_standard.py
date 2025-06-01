N,M=map(int,input().split())
flag=[input() for _ in range(N)]
ans=float('inf')
for w_end in range(1,N-1):
    for b_end in range(w_end+1,N):
        cnt=0
        for i in range(N):
            color='W' if i<w_end else 'B' if i<b_end else 'R'
            cnt+=sum(ch!=color for ch in flag[i])
        ans=min(ans,cnt)
print(ans)