item_count = int(input())

item_value_list = input().split()
for idx in range(item_count):
    item_value_list[idx] = int(item_value_list[idx])

item_cost_list = input().split()
for idx in range(item_count):
    item_cost_list[idx] = int(item_cost_list[idx])

item_profit_list = []
for idx in range(item_count):
    item_profit_list.append(item_value_list[idx] - item_cost_list[idx])

item_profit_list.sort(reverse=True)

total_profit = 0
for idx in range(item_count):
    if item_profit_list[idx] <= 0:
        break
    total_profit += item_profit_list[idx]

print(total_profit)