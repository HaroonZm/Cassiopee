A, B, X = map(int, input().split())
k, r = divmod(X, 1000)
ans = k * min(A, 2*B) + (min(A, 2*B) if r > 500 else min(A, B) if r > 0 else 0)
print(ans)