n = int(input())
A = list(map(int, input().split()))
k = 10000
C = [0] * (k + 1)
B = [0] * n
for x in A:
    C[x] += 1
for i in range(1, k + 1):
    C[i] += C[i - 1]
for x in reversed(A):
    B[C[x] - 1] = x
    C[x] -= 1
print(*B)