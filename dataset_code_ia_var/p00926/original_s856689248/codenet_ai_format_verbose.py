import sys

token_generator = (token for input_line in sys.stdin for token in input_line.split())

while True:
    try:
        number_of_elements = int(next(token_generator))
        number_of_operations = int(next(token_generator))
    except StopIteration:
        break

    element_values = [1] * (number_of_elements + 1)

    for operation_index in range(number_of_operations):
        interval_start_index = int(next(token_generator)) - 1
        interval_end_index = int(next(token_generator)) - 1

        for affected_element_index in range(interval_start_index, interval_end_index):
            element_values[affected_element_index] = 3

    print(sum(element_values))