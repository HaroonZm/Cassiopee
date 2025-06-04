input_value_a, input_value_b, input_value_c = map(int, input().split())
result_total = 0
complete_weeks = input_value_c // (7 * input_value_a + input_value_b)
remaining_tasks = input_value_c - complete_weeks * (7 * input_value_a + input_value_b)
if remaining_tasks <= 7 * input_value_a:
    print(7 * complete_weeks + (remaining_tasks + input_value_a - 1) // input_value_a)
else:
    print(7 * (complete_weeks + 1))