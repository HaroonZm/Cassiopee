MOD=10**9+7
n=int(input())
cards=[input().strip() for _ in range(n)]
lengths=[len(c) for c in cards]
pow10=[1]*(20*n+1)
for i in range(1,20*n+1):
    pow10[i]=(pow10[i-1]*10)%MOD
max_len=sum(lengths)
dp=[0]*(1<<n)
mult=[0]*(1<<n)
mult[0]=1
res=0
for mask in range(1<<n):
    for i in range(n):
        if mask&(1<<i)==0:
            new_mask=mask|(1<<i)
            val=(dp[mask]*pow10[lengths[i]]+mult[mask]*int(cards[i]))%MOD
            dp[new_mask]=(dp[new_mask]+val)%MOD
            mult[new_mask]=(mult[new_mask]+mult[mask])%MOD
for mask in range(1<<n):
    res=(res+dp[mask])%MOD
print(res)