N = int(input())
X = list(map(int, input().split()))
Y = sorted(X)
n = int(N // 2)
for e in X:
    if e <= Y[n - 1]:
        print(Y[n])
    elif e >= Y[n]:
        print(Y[n - 1])