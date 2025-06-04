S = []
for i in range(2020):
    S.append(0)

n = int(input())
X = input().split()
for i in range(n):
    X[i] = int(X[i])
    S[X[i]] = 1

m = int(input())
M = input().split()
for i in range(m):
    M[i] = int(M[i])

for i in range(m):
    idx = M[i] - 1
    if X[idx] + 1 != 2020:
        if S[X[idx]+1] == 0:
            S[X[idx]+1] = 1
            S[X[idx]] = 0
            X[idx] = X[idx] + 1

for i in range(2020):
    if S[i] == 1:
        print(i)