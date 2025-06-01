N, M = int(input()), int(input())
A = list(map(int, input().split()))
sc = [0] * N
for _ in range(M):
    B = list(map(int, input().split()))
    for a, b in zip(A, B):
        sc[b - 1 if a == b else a - 1] += 1
print(*sc)