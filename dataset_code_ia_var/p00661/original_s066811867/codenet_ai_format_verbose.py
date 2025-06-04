while True:

    number_of_elements, _ = map(int, raw_input().split())

    if number_of_elements == 0:
        break

    element_values = map(int, raw_input().split())

    minimum_element_value = min(element_values)

    if minimum_element_value > 1:
        result = number_of_elements / 2.0
    else:
        result = 0.0

    print result