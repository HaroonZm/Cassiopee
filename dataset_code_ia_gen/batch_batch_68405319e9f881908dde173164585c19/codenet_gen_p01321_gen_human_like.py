while True:
    n = int(input())
    if n == 0:
        break
    total_scores = []
    for _ in range(n):
        scores = list(map(int, input().split()))
        total_scores.append(sum(scores))
    print(max(total_scores), min(total_scores))