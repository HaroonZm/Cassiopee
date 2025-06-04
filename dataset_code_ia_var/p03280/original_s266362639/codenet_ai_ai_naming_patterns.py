input_first_value, input_second_value = map(int, input().split())
product_of_values = input_first_value * input_second_value
sum_of_modified_values = (1 * input_first_value) + (1 * input_second_value) - 1
final_result = product_of_values - sum_of_modified_values
print(final_result)