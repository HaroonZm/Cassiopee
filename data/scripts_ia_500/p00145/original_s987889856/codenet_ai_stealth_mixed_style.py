n = int(input())
C = list(map(lambda _: list(map(int, input().split())), range(n)))
W = {}
for i in range(n):
    W[i, i] = 0
for length in range(1, n):
    for start in range(n - length):
        end = start + length
        costs = []
        for mid in range(start, end):
            cost = C[start][0] * C[mid][1] * C[mid + 1][0] * C[end][1] + W[start, mid] + W[mid + 1, end]
            costs.append(cost)
        W[start, end] = min(costs)
print(W[0, n - 1])