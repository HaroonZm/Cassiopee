N,K=map(int,input().split())
hs = sorted([int(input()) for _ in range(N)])
ans = float("inf")
for i in range(N-K+1):
    ans = min(ans, hs[i+K-1]-hs[i])
print(ans)