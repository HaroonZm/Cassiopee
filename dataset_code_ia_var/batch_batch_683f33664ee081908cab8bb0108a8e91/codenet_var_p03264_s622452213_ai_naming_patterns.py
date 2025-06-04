user_input_value = int(input())
half_value = user_input_value // 2
is_odd_value = user_input_value % 2

if is_odd_value:
    result_value = half_value * (half_value + 1)
else:
    result_value = half_value ** 2

print(result_value)