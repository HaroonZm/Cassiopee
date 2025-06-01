N, M = int(input()), int(input())
A = list(map(int, input().split()))
S = [0] * N

from collections import Counter
for _ in range(M):
    B = list(map(int, input().split()))
    count_B = Counter(B)
    for j, b in enumerate(B):
        if b == A[j]:
            S[j] += 1
    for i, a in enumerate(A):
        S[a - 1] += N - count_B[a]

print(*S, sep='\n')