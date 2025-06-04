N, M = map(int, input().split())
A = [int(input()) for _ in range(N)]

for k in range(1, M + 1):
    for i in range(N - 1):
        if A[i] % k > A[i + 1] % k:
            A[i], A[i + 1] = A[i + 1], A[i]

for a in A:
    print(a)