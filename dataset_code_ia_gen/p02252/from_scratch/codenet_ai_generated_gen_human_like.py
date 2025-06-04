n, W = map(int, input().split())
items = []
for _ in range(n):
    v, w = map(int, input().split())
    items.append((v, w, v / w))

items.sort(key=lambda x: x[2], reverse=True)

total_value = 0.0
remaining_weight = W

for v, w, ratio in items:
    if remaining_weight == 0:
        break
    take_weight = min(w, remaining_weight)
    total_value += ratio * take_weight
    remaining_weight -= take_weight

print(f"{total_value:.9f}")