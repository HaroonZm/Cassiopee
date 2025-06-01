input_values_list = [int(input()) for input_index in range(5)]
first_value = input_values_list[0]
second_value = input_values_list[1]
third_value = input_values_list[2]
fourth_value = input_values_list[3]
fifth_value = input_values_list[4]

if first_value > 0:
    result_value = int(fifth_value * (second_value - first_value))
    print(result_value)
else:
    computed_value = abs(first_value) * third_value + fourth_value + second_value * fifth_value
    print(computed_value)