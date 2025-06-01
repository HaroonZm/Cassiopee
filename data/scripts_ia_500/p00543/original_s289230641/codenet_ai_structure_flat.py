N, M = map(int, input().split())
A = []
for _ in range(N):
    A.append(int(input()))
i = 1
while i <= M:
    if i != 1:
        j = 0
        while j < N - 1:
            if (A[j] % i) > (A[j+1] % i):
                tmp = A[j]
                A[j] = A[j+1]
                A[j+1] = tmp
            j += 1
    i += 1
index = 0
while index < N:
    print(A[index])
    index += 1