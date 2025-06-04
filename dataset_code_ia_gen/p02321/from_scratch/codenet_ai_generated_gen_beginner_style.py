N, W = map(int, input().split())
items = []
for _ in range(N):
    v, w = map(int, input().split())
    items.append((v, w))

max_value = 0

# On parcourt toutes les combinaisons possibles (2^N)
for mask in range(1 << N):
    total_value = 0
    total_weight = 0
    for i in range(N):
        if (mask & (1 << i)) != 0:
            total_value += items[i][0]
            total_weight += items[i][1]
    if total_weight <= W and total_value > max_value:
        max_value = total_value

print(max_value)