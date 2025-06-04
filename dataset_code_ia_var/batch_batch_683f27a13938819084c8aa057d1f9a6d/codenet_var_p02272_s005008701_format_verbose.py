import math

INFINITY_SENTINEL_VALUE = 1e9 + 1
merge_operation_counter = 0

def merge(sorted_sequence, left_index, mid_index, right_index):
    global merge_operation_counter

    left_subsequence = sorted_sequence[left_index:mid_index] + [INFINITY_SENTINEL_VALUE]
    right_subsequence = sorted_sequence[mid_index:right_index] + [INFINITY_SENTINEL_VALUE]

    left_pointer = 0
    right_pointer = 0

    for sorted_position in range(left_index, right_index):
        if left_subsequence[left_pointer] <= right_subsequence[right_pointer]:
            sorted_sequence[sorted_position] = left_subsequence[left_pointer]
            left_pointer += 1
        else:
            sorted_sequence[sorted_position] = right_subsequence[right_pointer]
            right_pointer += 1

    merge_operation_counter += right_index - left_index

def merge_sort(array_to_sort, left_index, right_index):
    if left_index + 1 < right_index:
        middle_index = (left_index + right_index) // 2

        merge_sort(array_to_sort, left_index, middle_index)
        merge_sort(array_to_sort, middle_index, right_index)
        merge(array_to_sort, left_index, middle_index, right_index)

number_of_elements = int(input())
input_sequence = list(map(int, input().split()))
merge_sort(input_sequence, 0, number_of_elements)
print(*input_sequence)
print(merge_operation_counter)