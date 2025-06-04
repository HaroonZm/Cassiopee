input_count_n, input_group_m = map(int, input().split())
array_values = list(map(int, input().split()))
index_current = 0
result_total = 0
while True:
    value_min = float('inf')
    value_max = 0
    for group_index in range(input_group_m):
        value_temp = array_values[index_current % input_count_n]
        value_min = min(value_min, value_temp)
        value_max = max(value_max, value_temp)
        index_current += 1
    result_total += value_max - value_min
    if index_current % input_count_n == 0:
        break
print(result_total)