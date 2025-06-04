n = int(input())
x = list(map(int, input().split()))

target = sorted(x)
visited = [False]*n
total_cost = 0

for i in range(n):
    if visited[i] or target[i] == x[i]:
        visited[i] = True
        continue
    cycle_sum = 0
    cycle_min = float('inf')
    cycle_len = 0
    j = i
    while not visited[j]:
        visited[j] = True
        weight = x[j]
        cycle_sum += weight
        if weight < cycle_min:
            cycle_min = weight
        j = x.index(target[j])
        cycle_len += 1
    if cycle_len > 1:
        total_cost += cycle_sum + (cycle_len - 2)*cycle_min

print(total_cost)