import sys
input=sys.stdin.readline

M,N=map(int,input().split())
P=[int(input()) for _ in range(M)]
boxes=[tuple(map(int,input().split())) for _ in range(N)]

P.sort(reverse=True)

max_c=max(c for c,_ in boxes)
prefix=[0]*(min(M,max_c)+1)
for i in range(1,len(prefix)):
    prefix[i]=prefix[i-1]+P[i-1]

dp=[0]*(1<<N) if N<=20 else None  # N can be up to 500, cannot use subset DP

# Because N up to 500, subset DP impossible. Use 0/1 knapsack approach on box selection based on capacity (total manju)

# Each box used at most once, selecting subset to maximize sum(prefix[c_j])-sum(E_j)
# Capacity is unbounded (up to sum C_j), but total manju to pack is <= M.

# Let's do DP on boxes to get best profit for each possible total manju count.

# dp[i]: max profit achieving packing exactly i manju in some subset of boxes
dp_profit=[-10**15]*(M+1)
dp_profit[0]=0
for c,e in boxes:
    for i in range(M,c-1,-1):
        val=prefix[c]-e
        if dp_profit[i-c]+val>dp_profit[i]:
            dp_profit[i]=dp_profit[i-c]+val

print(max(0,max(dp_profit)))