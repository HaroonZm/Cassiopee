N, M = map(int, input().split())
A = [int(input()) for _ in range(N)]
B = [int(input()) for _ in range(M)]

votes = [0] * N

for b in B:
    for i in range(N):
        if A[i] <= b:
            votes[i] += 1
            break

max_votes = max(votes)
for i in range(N):
    if votes[i] == max_votes:
        print(i + 1)
        break