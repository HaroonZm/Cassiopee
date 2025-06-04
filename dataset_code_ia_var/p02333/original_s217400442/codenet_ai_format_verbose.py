number_of_elements, combination_size = map(int, input().split(" "))

if number_of_elements < combination_size:
    print(0)
else:
    coefficients_list = [1, 0]

    for current_index in range(number_of_elements):
        new_coefficients_list = [0]
        for inner_index in range(1, len(coefficients_list)):
            new_value = coefficients_list[inner_index - 1] + (inner_index * coefficients_list[inner_index])
            new_coefficients_list.append(new_value)
        new_coefficients_list.append(0)
        coefficients_list = new_coefficients_list

    for multiplier in range(1, combination_size + 1):
        coefficients_list[combination_size] *= multiplier

    result = coefficients_list[combination_size] % (10**9 + 7)
    print(result)