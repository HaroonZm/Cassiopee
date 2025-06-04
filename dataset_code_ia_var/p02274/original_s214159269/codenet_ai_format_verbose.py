def swap_elements_and_count(list_to_sort, index_first, index_second, inversion_count):
    if list_to_sort[index_second] < list_to_sort[index_first]:
        list_to_sort[index_first], list_to_sort[index_second] = list_to_sort[index_second], list_to_sort[index_first]
        inversion_count[0] += 1
        return 1
    return 0


def merge_sorted_intervals(list_to_sort, left_start, right_start, right_end, inversion_count):
    left_pointer = left_start
    right_pointer = right_start
    merged_list = []

    while True:
        if list_to_sort[left_pointer] <= list_to_sort[right_pointer]:
            merged_list.append(list_to_sort[left_pointer])
            left_pointer += 1
        else:
            merged_list.append(list_to_sort[right_pointer])
            right_pointer += 1
            inversion_count[0] += right_start - left_pointer

        if left_pointer == right_start:
            for current_index in range(right_pointer, right_end):
                merged_list.append(list_to_sort[current_index])
            break

        if right_pointer == right_end:
            for current_index in range(left_pointer, right_start):
                merged_list.append(list_to_sort[current_index])
            break

    for result_index in range(left_start, right_end):
        list_to_sort[result_index] = merged_list[result_index - left_start]


def merge_sort_and_count(list_to_sort, segment_left, segment_right, inversion_count):
    if segment_right == segment_left:
        return

    if segment_left + 1 == segment_right:
        swap_elements_and_count(list_to_sort, segment_left, segment_right, inversion_count)
    else:
        segment_middle = (segment_left + segment_right) // 2

        merge_sort_and_count(list_to_sort, segment_left, segment_middle, inversion_count)
        merge_sort_and_count(list_to_sort, segment_middle + 1, segment_right, inversion_count)

        merge_sorted_intervals(list_to_sort, segment_left, segment_middle + 1, segment_right + 1, inversion_count)


number_of_elements = int(input())
input_numbers = list(map(int, input().split()))
total_inversion_count = [0]

merge_sort_and_count(input_numbers, 0, number_of_elements - 1, total_inversion_count)

print(total_inversion_count[0])