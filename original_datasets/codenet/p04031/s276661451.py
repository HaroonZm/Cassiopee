n = int(input())
a = list(map(int, input().split()))
max = max(a)
min = min(a)
cost_min = n * (max - min)**2
for m in range(min, max+1):
    cost = 0
    for x in a:
        cost += (x - m)**2
    if cost < cost_min:
        cost_min = cost
print(cost_min)