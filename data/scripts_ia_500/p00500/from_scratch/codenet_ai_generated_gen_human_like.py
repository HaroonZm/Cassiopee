n = int(input())
scores = [list(map(int, input().split())) for _ in range(n)]

result = [0] * n

for round in range(3):
    counts = {}
    for i in range(n):
        counts[scores[i][round]] = counts.get(scores[i][round], 0) + 1
    for i in range(n):
        if counts[scores[i][round]] == 1:
            result[i] += scores[i][round]

for total in result:
    print(total)