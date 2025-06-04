elem_count = int(input())
value_list = list(map(int, input().split()))
cost_list = list(map(int, input().split()))
total_difference_sum = 0
for idx in range(elem_count):
    difference = value_list[idx] - cost_list[idx]
    if difference > 0:
        total_difference_sum += difference
print(total_difference_sum)