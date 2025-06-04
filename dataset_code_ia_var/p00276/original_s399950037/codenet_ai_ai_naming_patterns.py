user_input_count = input()
for iteration_index in [1] * user_input_count:
    value_c, value_a, value_n = map(int, raw_input().split())
    score_total = 0
    while value_c > 0 and value_a > 0 and value_n > 0:
        score_total += 1
        value_c, value_a, value_n = value_c - 1, value_a - 1, value_n - 1
    while value_c > 0 and value_a > 0:
        score_total += 1
        value_c, value_a = value_c - 2, value_a - 1
    print score_total + value_c / 3