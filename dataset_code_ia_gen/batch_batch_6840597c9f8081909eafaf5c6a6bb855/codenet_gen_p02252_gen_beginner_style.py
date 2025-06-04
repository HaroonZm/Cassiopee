N, W = map(int, input().split())
items = []
for _ in range(N):
    v, w = map(int, input().split())
    items.append((v, w))

# Calculate value per weight for each item
for i in range(N):
    v, w = items[i]
    items[i] = (v, w, v / w)

# Sort items by value per weight descending
items.sort(key=lambda x: x[2], reverse=True)

total_value = 0.0
capacity = W

for v, w, ratio in items:
    if capacity == 0:
        break
    if w <= capacity:
        total_value += v
        capacity -= w
    else:
        total_value += ratio * capacity
        capacity = 0

print(total_value)