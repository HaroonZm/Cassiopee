N, M = map(int, input().split())
A = [int(input()) for _ in range(N)]

for k in range(2, M + 1):
    i = 0
    while i < N - 1:
        if (A[i] % k) > (A[i + 1] % k):
            A[i], A[i + 1] = A[i + 1], A[i]
            i += 1
        i += 1

for num in A:
    print(num)