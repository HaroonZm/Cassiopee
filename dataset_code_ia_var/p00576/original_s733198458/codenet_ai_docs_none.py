S = [0]*2020
n = int(input())
X = [int(a) for a in input().split()]
for a in X:
    S[a] = 1
m = int(input())
M = [int(a) for a in input().split()]
for i in M:
    i = i - 1
    if X[i]+1 != 2020:
        if S[X[i]+1] == 0:
            S[X[i]+1] = 1
            S[X[i]] = 0
            X[i] = X[i]+1
for i in range(2020):
    if S[i] == 1:
        print(i)