N=int(input())
lines=[input() for _ in range(N)]
label_pos={}
for i,s in enumerate(lines):
    if s.endswith(':'):
        label_pos[s[:-1]]=i
dp=[-1]*(N+1)
def f(i):
    if i==N: return 0
    if dp[i]>=0: return dp[i]
    s=lines[i]
    if s.endswith(':'):
        dp[i]=f(i+1)
    else:
        tgt=label_pos[s[5:-1]]
        # remove goto
        dp[i]=1+f(i+1)
        # keep goto
        dp[i]=min(dp[i],f(tgt))
    return dp[i]
print(f(0))