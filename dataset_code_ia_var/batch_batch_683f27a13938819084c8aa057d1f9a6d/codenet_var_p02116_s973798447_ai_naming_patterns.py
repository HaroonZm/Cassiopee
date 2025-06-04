input_number = int(input())
incremented_number = input_number + 1
negated_bitwise_not_number = -~incremented_number
bitwise_and_result = incremented_number & negated_bitwise_not_number
print(bitwise_and_result)