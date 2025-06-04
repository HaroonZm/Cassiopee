N = int(input())
X = list(map(int, input().split()))
M = int(input())
A = list(map(int, input().split()))

for i in range(M):
    idx = A[i] - 1
    if X[idx] != 2019 and (X[idx] + 1) not in X:
        X[idx] = X[idx] + 1

for num in X:
    print(num)