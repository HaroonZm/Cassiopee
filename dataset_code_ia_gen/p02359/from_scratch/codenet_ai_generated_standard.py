N, T = map(int, input().split())
times = [0]*(T+1)
for _ in range(N):
    l, r = map(int, input().split())
    times[l] += 1
    times[r] -= 1
max_customers = current = 0
for i in range(T):
    current += times[i]
    if current > max_customers:
        max_customers = current
print(max_customers)