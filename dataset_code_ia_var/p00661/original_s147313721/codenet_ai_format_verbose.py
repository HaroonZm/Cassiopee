while True:

    number_of_elements, _ = map(int, input().split())

    if number_of_elements == 0:
        break

    element_values = list(map(int, input().split()))
    sorted_element_values = sorted(element_values)

    is_first_element_one = (sorted_element_values[0] == 1)
    result_flag = 0 if is_first_element_one else 1

    if result_flag:
        computed_result = number_of_elements / 2
    else:
        computed_result = 0

    print('{:.10f}'.format(computed_result))