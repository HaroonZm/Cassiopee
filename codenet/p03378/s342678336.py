N, M, X = map(int, input().split())
A = list(map(int, input().split()))

cost_a, cost_b = 0, 0

for i in range(X, N):
    if i in A:
        cost_a += 1
for i in range(0, X):
    if i in A:
        cost_b += 1
print(min(cost_b, cost_a))