N, M = map(int, input().split())
A = [int(input()) for _ in range(N)]
B = [int(input()) for _ in range(M)]

votes = [0] * N

for b in B:
    for i in range(N):
        if A[i] <= b:
            votes[i] += 1
            break

print(votes.index(max(votes)) + 1)