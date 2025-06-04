input_first_val, input_second_val = map(int, input().split())
result_total = 0
for current_val in [input_first_val, input_second_val]:
    if current_val == 3:
        result_total += 10**5
    elif current_val == 2:
        result_total += 2 * 10**5
    elif current_val == 1:
        result_total += 3 * 10**5
if input_first_val == 1 and input_second_val == 1:
    result_total += 4 * 10**5
print(result_total)