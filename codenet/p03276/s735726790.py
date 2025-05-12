N, K = map(int, input().split())
X = list(map(int, input().split()))
ans = float("inf")
for i in range(N-K+1):
    a, b = X[i], X[i+K-1]
    ans = min(ans, b-a+min(abs(a),abs(b)))
print(ans)