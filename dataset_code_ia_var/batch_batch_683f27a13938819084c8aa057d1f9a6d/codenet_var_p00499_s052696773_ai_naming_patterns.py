input_length = int(input())
item_count_a = int(input())
item_count_b = int(input())
capacity_a = int(input())
capacity_b = int(input())

if item_count_a % capacity_a == 0 and item_count_b % capacity_b == 0:
    days_a = item_count_a // capacity_a
    days_b = item_count_b // capacity_b
    min_days, max_days = sorted([days_a, days_b])
    print(input_length - max_days)
elif item_count_a % capacity_a == 0 and item_count_b % capacity_b != 0:
    days_a = item_count_a // capacity_a
    days_b = (item_count_b // capacity_b) + 1
    min_days, max_days = sorted([days_a, days_b])
    print(input_length - max_days)
elif item_count_a % capacity_a != 0 and item_count_b % capacity_b == 0:
    days_a = (item_count_a // capacity_a) + 1
    days_b = item_count_b // capacity_b
    min_days, max_days = sorted([days_a, days_b])
    print(input_length - max_days)
else:
    days_a = (item_count_a // capacity_a) + 1
    days_b = (item_count_b // capacity_b) + 1
    min_days, max_days = sorted([days_a, days_b])
    print(input_length - max_days)