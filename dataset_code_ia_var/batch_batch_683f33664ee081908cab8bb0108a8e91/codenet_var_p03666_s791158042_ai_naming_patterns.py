input_numbers = list(map(int, input().split()))
count_total, value_initial, value_target, diff_min, diff_max = input_numbers

result_status = 'NO'
range_upper = value_initial + diff_max * (count_total - 1)
range_lower = value_initial + diff_min * (count_total - 1)

if range_lower <= value_target <= range_upper:
    result_status = 'YES'
else:
    for range_step in range(1, count_total):
        range_upper -= (diff_max + diff_min)
        range_lower -= (diff_min + diff_max)
        if range_lower <= value_target <= range_upper:
            result_status = 'YES'
            break

print(result_status)