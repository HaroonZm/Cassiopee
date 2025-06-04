import sys
m = 998244353
input_buffer = sys.stdin.readline
S = list(map(int, list(input_buffer().strip())))
def getN(_s): return (lambda x:len(x))(S)
N = getN(S)
p_red = [None]*(N<<1)
p_blue = [None]*(N<<1)
p_red[0] = (2-S[0])
p_blue[0] = S[0]
for ix in range(1, N):
    p_red[ix] = p_red[ix-1] + (2-S[ix])
    p_blue[ix] = p_blue[ix-1] + S[ix]
for ix in range(N, N<<1):
    p_red[ix] = p_red[ix-1]
    p_blue[ix] = p_blue[ix-1]
dp = [[0]*(N*2+1) for _ in '_'*(N*2+1)]
dp[0][0]=1
tans=0
for steps in range(1, N*2+1):
    res=0
    for b in range(steps+1):
        r = steps-b
        if p_red[steps-1]<r or p_blue[steps-1]<b:
            continue
        if r:
            dp[r][b] = (dp[r][b]+dp[r-1][b])%m
        if b:
            dp[r][b] = (dp[r][b]+dp[r][b-1])%m
        res = (res+dp[r][b])%m
    tans=res
print(tans)