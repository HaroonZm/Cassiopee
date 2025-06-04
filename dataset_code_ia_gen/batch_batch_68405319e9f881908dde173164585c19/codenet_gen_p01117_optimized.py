while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    totals = [0]*n
    for _ in range(m):
        scores = list(map(int, input().split()))
        for i in range(n):
            totals[i] += scores[i]
    print(max(totals))