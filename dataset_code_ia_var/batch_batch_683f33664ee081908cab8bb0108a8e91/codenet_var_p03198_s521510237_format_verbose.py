from sys import stdin
from itertools import repeat

def compute_operations_list(input_list):
    list_length = len(input_list)
    operation_count_list = [0] * (list_length + 1)
    state_stack = [(input_list[0], input_list[0], 1)]
    stack_append = state_stack.append
    stack_pop = state_stack.pop

    for current_index in xrange(1, list_length):
        accumulated_operations = 0
        current_value = input_list[current_index]
        merged_count = 1

        while state_stack and current_value > state_stack[-1][0]:
            previous_base, previous_top, previous_count = stack_pop()
            operation_increment = 0

            while previous_base < current_value:
                previous_base *= 4
                operation_increment += 2

            accumulated_operations += operation_increment * previous_count
            merged_count += previous_count
            current_value = previous_top << operation_increment

        stack_append((input_list[current_index], current_value, merged_count))
        operation_count_list[current_index + 1] = operation_count_list[current_index] + accumulated_operations

    return operation_count_list

def main():
    number_of_elements = int(stdin.readline())
    input_values = map(int, stdin.readline().split(), repeat(10, number_of_elements))
    prefix_operations = compute_operations_list(input_values)
    suffix_operations = compute_operations_list(input_values[::-1])[::-1]
    minimal_total_operations = 10 ** 12

    for split_index in xrange(number_of_elements + 1):
        total_operations = prefix_operations[split_index] + split_index + suffix_operations[split_index]
        if minimal_total_operations > total_operations:
            minimal_total_operations = total_operations

    print minimal_total_operations

main()