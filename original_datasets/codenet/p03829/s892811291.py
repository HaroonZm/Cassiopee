N, A, B = map(int, input().split())
X = list(map(int, input().split()))
ans = sum([min(A * (X[i+1]-X[i]), B) for i in range(N-1)])
print(ans)