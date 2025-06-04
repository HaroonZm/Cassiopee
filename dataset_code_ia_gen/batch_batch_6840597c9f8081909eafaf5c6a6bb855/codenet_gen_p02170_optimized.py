MOD=998244353
def modinv(x):
    return pow(x,MOD-2,MOD)
N,K,A=map(int,input().split())
inv100=modinv(100)
p=(A*inv100)%MOD
q=(1-p)%MOD
invN=modinv(N)
dp=[0]*(K+N+1)
sm=0
for i in range(K,K+N):
    dp[i]=1
for i in range(K-1,-1,-1):
    sm+=dp[i+1]-dp[i+N+1]
    sm%=MOD
    dp[i]=(p+q*sm*invN)%MOD
print(dp[0])