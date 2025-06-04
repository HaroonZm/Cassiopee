N = int(input())
M = int(input())
if N % 2:
    print(1 + (N - 1) / 2 + (100 - M) * (N + 1) / 2 / M)
else:
    print(N * 50 / M)