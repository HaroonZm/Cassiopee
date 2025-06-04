N, K = list(map(int, input().split()))
H = [int(input()) for _ in range(N)]
H.sort()
ans = []
for i in range(N-K+1):
    ans.append(H[i+K-1]-H[i])
print(min(ans))