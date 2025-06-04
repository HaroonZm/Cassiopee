N = int(input())

X = int(N / 1.08)
if X * 1.08 < N:
    X = X + 1

if int(X * 1.08) == N:
    print(X)
else:
    print(":(")