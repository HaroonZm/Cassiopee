value_a, value_b, value_x = [int(input_value) for input_value in input().split()]

if value_x >= value_a:
    result_temp = ((value_x - value_b) // (value_a - value_b)) * value_b + value_x
else:
    result_temp = value_x

result_modulo = result_temp % 1000000007

print(result_modulo)