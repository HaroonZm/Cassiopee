import sys
import bisect

query_count = int(input())
input_lines = sys.stdin.readlines()
output_list = [None] * query_count
ordered_elements = []

for query_index in range(query_count):
    operation_code, *operation_args = input_lines[query_index].split()
    target_value = int(operation_args[0])
    left_position = bisect.bisect_left(ordered_elements, target_value)
    right_position = bisect.bisect_right(ordered_elements, target_value)

    if operation_code == '0':  # insert
        ordered_elements.insert(left_position, target_value)
        output_list[query_index] = str(len(ordered_elements))
    elif operation_code == '1':  # find count
        output_list[query_index] = right_position - left_position
    elif operation_code == '2':  # delete all
        ordered_elements[left_position:right_position] = []
    else:  # dump range
        range_right = bisect.bisect_right(ordered_elements, int(operation_args[1]))
        if left_position != range_right:
            output_list[query_index] = '\n'.join(map(str, ordered_elements[left_position:range_right]))
        else:
            output_list[query_index] = None

for output_item in output_list:
    if output_item is not None:
        print(output_item)