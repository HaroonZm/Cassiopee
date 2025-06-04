input_n, input_a, input_b, input_c, input_d = map(int, input().split())

is_div_a = input_n % input_a == 0
is_div_c = input_n % input_c == 0

if is_div_a and is_div_c:
    cost_a = (input_n // input_a) * input_b
    cost_c = (input_n // input_c) * input_d
elif is_div_a and not is_div_c:
    cost_a = (input_n // input_a) * input_b
    cost_c = ((input_n // input_c) + 1) * input_d
elif not is_div_a and is_div_c:
    cost_a = ((input_n // input_a) + 1) * input_b
    cost_c = (input_n // input_c) * input_d
else:
    cost_a = ((input_n // input_a) + 1) * input_b
    cost_c = ((input_n // input_c) + 1) * input_d

min_cost, _ = sorted([cost_a, cost_c])
print(min_cost)