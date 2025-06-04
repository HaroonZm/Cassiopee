count_items = int(input())
item_values = list(map(int, input().split()))
current_money = 1000
current_stock = 0

for idx in range(count_items):
    if idx != count_items - 1:
        if item_values[idx] <= item_values[idx + 1]:
            current_money += item_values[idx] * current_stock
            current_stock = current_money // item_values[idx]
            current_money -= current_stock * item_values[idx]
        else:
            current_money += item_values[idx] * current_stock
            current_stock = 0
    else:
        current_money += item_values[idx] * current_stock

print(current_money)