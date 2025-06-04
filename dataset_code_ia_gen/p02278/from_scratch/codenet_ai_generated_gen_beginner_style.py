n = int(input())
w = list(map(int, input().split()))

sorted_w = sorted(w)
index_map = {v: i for i, v in enumerate(sorted_w)}

visited = [False] * n
total_cost = 0
global_min = sorted_w[0]

for i in range(n):
    if visited[i] or index_map[w[i]] == i:
        continue
    cycle_sum = 0
    cycle_min = 10**9
    cycle_len = 0
    j = i
    while not visited[j]:
        visited[j] = True
        val = w[j]
        cycle_sum += val
        if val < cycle_min:
            cycle_min = val
        j = index_map[val]
        cycle_len += 1
    if cycle_len > 1:
        cost1 = cycle_sum + (cycle_len - 2) * cycle_min
        cost2 = cycle_sum + cycle_min + (cycle_len + 1) * global_min
        total_cost += min(cost1, cost2)

print(total_cost)