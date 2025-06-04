comparison_count = 0

def merge_sort(input_array):

    global comparison_count

    if len(input_array) <= 1:
        return input_array

    middle_index = len(input_array) // 2

    left_subarray = input_array[:middle_index]
    right_subarray = input_array[middle_index:]

    comparison_count += len(left_subarray) + len(right_subarray)

    sorted_left = merge_sort(left_subarray)
    sorted_right = merge_sort(right_subarray)

    return merge_sorted_arrays(sorted_left, sorted_right)


def merge_sorted_arrays(sorted_left_array, sorted_right_array):

    merged_array = []
    left_pointer = 0
    right_pointer = 0

    while left_pointer < len(sorted_left_array) and right_pointer < len(sorted_right_array):

        if sorted_left_array[left_pointer] <= sorted_right_array[right_pointer]:
            merged_array.append(sorted_left_array[left_pointer])
            left_pointer += 1
        else:
            merged_array.append(sorted_right_array[right_pointer])
            right_pointer += 1

    if left_pointer < len(sorted_left_array):
        merged_array.extend(sorted_left_array[left_pointer:])

    if right_pointer < len(sorted_right_array):
        merged_array.extend(sorted_right_array[right_pointer:])

    return merged_array


number_of_elements = int(input())

unsorted_list = list(map(int, input().split()))

sorted_list = merge_sort(unsorted_list)

print(" ".join(map(str, sorted_list)))
print(comparison_count)