from bisect import bisect_left
def inpl(): return list(map(int, input().split()))

N, M = inpl()
X = inpl()
Q = int(input())
L = inpl()

X += [N+1]
initcost = X[0] - 1
costs = [X[i+1] - X[i] - 1 for i in range(M) if X[i+1] - X[i] > 1]
C = [0]*(N+1)
C[0] = - 10**9

for i in range(1, N+1):
    cost = 0
    costs2 = []
    for c in costs:
        cost += c
        if c > 1:
            costs2.append(c-1)
    C[i] = - (initcost + cost)
    costs = costs2

for l in L:
    if l < - C[-1]:
        print(-1)
    else:
        print(bisect_left(C, -l))