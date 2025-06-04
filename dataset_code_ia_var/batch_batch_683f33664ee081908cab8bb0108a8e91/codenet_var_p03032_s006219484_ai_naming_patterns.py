import heapq

def main():
    item_count, operation_limit = map(int, input().split())
    item_values = list(map(int, input().split()))

    max_score = 0
    take_distributions = []

    for discard_count in range(101):
        for left_take_count in range(101):
            for right_take_count in range(101):
                if discard_count + left_take_count + right_take_count <= operation_limit and left_take_count + right_take_count <= item_count:
                    take_distributions.append((left_take_count, right_take_count, discard_count))

    for left_count, right_count, discard_count in take_distributions:
        selected_items = []
        for i in range(left_count):
            selected_items.append(item_values[i])
        for i in range(right_count):
            selected_items.append(item_values[-(i + 1)])
        heapq.heapify(selected_items)
        for _ in range(min(discard_count, left_count + right_count)):
            heapq.heappop(selected_items)
        max_score = max(max_score, sum(selected_items))

    print(max_score)

main()