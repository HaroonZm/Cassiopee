N = int(input())
scores = list(map(int, input().split()))

max_score = 0
for A in range(1, N + 1):
    count = sum(1 for s in scores if s >= A)
    if count >= A:
        max_score = A

print(max_score)