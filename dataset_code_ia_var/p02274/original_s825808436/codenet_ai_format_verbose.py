global number_of_inversions
number_of_inversions = 0

def merge(
    array_to_sort,
    left_index,
    middle_index,
    right_index
):
    left_subarray = array_to_sort[left_index:middle_index]
    right_subarray = array_to_sort[middle_index:right_index]

    left_subarray.append(float("inf"))
    right_subarray.append(float("inf"))

    left_pointer = 0
    right_pointer = 0

    for current_index in range(left_index, right_index):
        global number_of_inversions

        if left_subarray[left_pointer] <= right_subarray[right_pointer]:
            array_to_sort[current_index] = left_subarray[left_pointer]
            left_pointer += 1
        else:
            array_to_sort[current_index] = right_subarray[right_pointer]
            right_pointer += 1
            number_of_inversions += (middle_index - left_index - left_pointer)

def merge_sort(
    array_to_sort,
    left_index,
    right_index
):
    if left_index + 1 < right_index:
        middle_index = int((left_index + right_index) / 2)
        merge_sort(array_to_sort, left_index, middle_index)
        merge_sort(array_to_sort, middle_index, right_index)
        merge(array_to_sort, left_index, middle_index, right_index)

number_of_elements = int(input())
elements_to_sort = list(map(int, input().split()))

merge_sort(
    elements_to_sort,
    left_index=0,
    right_index=number_of_elements
)

print(number_of_inversions)