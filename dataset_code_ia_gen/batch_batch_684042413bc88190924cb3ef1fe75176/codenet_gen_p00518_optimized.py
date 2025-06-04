N=int(input())
S=input()
MOD=10007
members={'J':1,'O':2,'I':4}
dp=[ [0]*8 for _ in range(N+1)]
dp[0][1]=1
for i in range(N):
    r=members[S[i]]
    for prev_keys in range(8):
        if dp[i][prev_keys]==0:
            continue
        for now_keys in range(1,8):
            if (now_keys & r)==0:
                continue
            if (prev_keys & now_keys)==0:
                continue
            dp[i+1][now_keys]=(dp[i+1][now_keys]+dp[i][prev_keys])%MOD
print(sum(dp[N])%MOD)