N = int(input())
points = list(map(int, input().split()))

score = 0
for A in range(1, N + 1):
    count = sum(1 for p in points if p >= A)
    if count >= A:
        score = A

print(score)