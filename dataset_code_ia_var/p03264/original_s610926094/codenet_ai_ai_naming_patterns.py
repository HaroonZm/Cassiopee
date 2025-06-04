input_value = int(input())
if input_value % 2 == 0:
    result_value = (input_value ** 2) // 4
else:
    result_value = (input_value ** 2 - 1) // 4
print(result_value)