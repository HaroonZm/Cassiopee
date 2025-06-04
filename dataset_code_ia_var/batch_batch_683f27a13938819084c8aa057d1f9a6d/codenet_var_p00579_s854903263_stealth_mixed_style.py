N, M = (int(x) for x in input().split())
L = [None]*M
R = [None]*M
A = [int(z) for z in input().split()]

for idx in range(M):
    x,y = input().split()
    L[idx]=int(x)
    R[idx]=int(y)

pre = [*range(0,N+1)]
dp = [0 for _ in range(N+1)]

def update_pre(pre, R, L):
    for c in range(len(R)):
        if pre[R[c]]>L[c]-1:
            pre[R[c]]=L[c]-1
update_pre(pre, R, L)

for position in range(N-1,0,-1):
    pre[position] = min(pre[position], pre[position+1])

result = 0
i=1
while i<=N:
    x = dp[i-1] if dp[i-1]>dp[pre[i]]+A[i-1] else dp[pre[i]]+A[i-1]
    dp[i]=x
    i+=1
else:
    result = dp[N]

print(result)