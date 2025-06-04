n_k = input().split()
N = int(n_k[0])
K = int(n_k[1])
A = input().split()
for i in range(N):
    A[i] = int(A[i])

if K == 1:
    print(0)
    exit()

min_cost = 10**12

for b in range(1<<(N-1)):
    h = A[0]
    k = 1
    cost = 0
    for i in range(N-1):
        a = A[i+1]
        if a > h:
            k += 1
            h = a
        elif (b & (1 << i)):
            k += 1
            cost += (h + 1) - a
            h += 1
    if k >= K:
        if cost < min_cost:
            min_cost = cost

print(min_cost)