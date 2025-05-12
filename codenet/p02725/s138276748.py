##### ABC 160
K,N = map(int, input().split())
A = list(map(int,input().split()))

dist = []
for i in range(N-1):
    dist.append(A[i+1]-A[i])
    
dist.append(K-A[-1]+A[0])

dist.sort()

ans = 0
for i in range(N-1):
    ans += dist[i]
    
print(ans)