input_value = int(input())

half_value = input_value // 2

if input_value % 2 == 0:
    result_value = half_value ** 2
else:
    result_value = half_value * (half_value + 1)

print(result_value)