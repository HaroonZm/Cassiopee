N, M = map(int, input().split())
costs = []
prizes = 0
for _ in range(M):
    A, B = map(int, input().split())
    if A >= N:
        prizes += 1
    else:
        costs.append(N - A)
costs.sort()
needed = M - 1 - prizes
print(sum(costs[:needed]) if needed > 0 else 0)