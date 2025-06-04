n = int(input())
A = list(map(int, input().split()))

k = 10000
C = [0] * (k + 1)
B = [0] * n

for x in A:
    C[x] += 1

for i in range(1, k + 1):
    C[i] += C[i - 1]

for j in range(n - 1, -1, -1):
    B[C[A[j]] - 1] = A[j]
    C[A[j]] -= 1

print(' '.join(map(str, B)))