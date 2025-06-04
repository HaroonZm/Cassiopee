import sys

SENTINEL_VALUE = 1000000001

def merge_sort_and_count_inversions(array, left_index, right_index):
    if left_index + 1 < right_index:
        middle_index = (left_index + right_index) // 2
        
        inversion_count_left = merge_sort_and_count_inversions(array, left_index, middle_index)
        inversion_count_right = merge_sort_and_count_inversions(array, middle_index, right_index)
        inversion_count_merge = merge_and_count(array, left_index, middle_index, right_index)
        
        return inversion_count_left + inversion_count_right + inversion_count_merge
    
    else:
        return 0

def merge_and_count(array, left_index, middle_index, right_index):
    number_of_elements_left = len(array[left_index:middle_index])
    
    left_subarray = array[left_index:middle_index] + [SENTINEL_VALUE]
    right_subarray = array[middle_index:right_index] + [SENTINEL_VALUE]
    
    left_pointer = 0
    right_pointer = 0
    inversion_count = 0
    
    for merged_index in range(left_index, right_index):
        if left_subarray[left_pointer] <= right_subarray[right_pointer]:
            array[merged_index] = left_subarray[left_pointer]
            left_pointer += 1
        else:
            inversion_count += number_of_elements_left - left_pointer
            array[merged_index] = right_subarray[right_pointer]
            right_pointer += 1
            
    return inversion_count

number_of_elements = int(sys.stdin.readline())
input_array = list(map(int, sys.stdin.readline().split()))

total_inversions = merge_sort_and_count_inversions(input_array, 0, number_of_elements)

print(total_inversions)