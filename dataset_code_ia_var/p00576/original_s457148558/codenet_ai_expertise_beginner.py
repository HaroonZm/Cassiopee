N = int(input())
X = list(map(int, input().split()))
M = int(input())
A = list(map(int, input().split()))

for j in range(M):
    idx = A[j] - 1
    if (X[idx] + 1) in X or X[idx] == 2019:
        continue
    else:
        X[idx] = X[idx] + 1

for k in range(N):
    print(X[k])