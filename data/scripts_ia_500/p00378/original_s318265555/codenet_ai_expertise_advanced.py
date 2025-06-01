from math import ceil

A, B, X = map(int, input().split())

if A < B:
    print(A * ceil(X / 1000))
elif A < 2 * B:
    remainder = X % 1000
    print(A * (X // 1000) + (B if remainder and remainder <= 500 else A if remainder > 500 else 0))
else:
    print(B * ceil(X / 500))