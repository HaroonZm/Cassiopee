from bisect import bisect_left

N, M = map(int, input().split())
X = list(map(int, input().split()))
Q = int(input())
L = list(map(int, input().split()))

X.append(N+1)
initcost = X[0] - 1
costs = []
for i in range(M):
    d = X[i+1] - X[i]
    if d > 1:
        costs.append(d - 1)
C = [0] * (N+1)
C[0] = -10**9
i = 1
cur_costs = costs[:]  # auxiliary copy as we overwrite
while i <= N:
    cost = 0
    costs2 = []
    for c in cur_costs:
        cost += c
        if c > 1:
            costs2.append(c-1)
    C[i] = - (initcost + cost)
    cur_costs = costs2
    i += 1

for l in L:
    if l < -C[-1]:
        print(-1)
    else:
        print(bisect_left(C, -l))