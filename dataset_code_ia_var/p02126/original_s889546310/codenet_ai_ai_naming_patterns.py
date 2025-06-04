import heapq

item_count, total_wanted, category_count = map(int, input().split())
category_heaps = [[] for _ in range(category_count + 1)]
category_limits = [0] + list(map(int, input().split()))

for _ in range(item_count):
    item_category, item_weight = map(int, input().split())
    heapq.heappush(category_heaps[item_category], item_weight)
    if len(category_heaps[item_category]) > category_limits[item_category]:
        heapq.heappop(category_heaps[item_category])

all_selected_items = [weight for heap in category_heaps for weight in heap]
all_selected_items.sort()
final_answer = sum(all_selected_items[-total_wanted:])
print(final_answer)