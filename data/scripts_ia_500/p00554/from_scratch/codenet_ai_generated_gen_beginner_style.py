N, M = map(int, input().split())
costs = []
count = 0

for _ in range(M):
    A, B = map(int, input().split())
    if A >= N:
        count += 1
    else:
        costs.append(N - A)

costs.sort()

need = M - 1 - count
if need <= 0:
    print(0)
else:
    print(sum(costs[:need]))