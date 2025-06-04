input_number = int(input())
result_value = 1
for loop_index in range(input_number):
    result_value = (result_value * (loop_index + 1)) % (10**9 + 7)
print(result_value)