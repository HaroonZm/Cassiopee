N, A, B = map(int, input().split())
X = [int(_) for _ in input().split()]
F = 0
for i in range(1, N):
    if A * (X[i] - X[i-1]) >= B:
        F += B
    else:
        F += A * (X[i] - X[i-1])
print(F)