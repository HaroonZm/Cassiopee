def merge_and_count_inversions(input_list):
    if len(input_list) == 1:
        return input_list, 0

    middle_index = len(input_list) // 2

    left_half, left_inversions = merge_and_count_inversions(input_list[:middle_index])
    right_half, right_inversions = merge_and_count_inversions(input_list[middle_index:])

    total_inversions = 0
    merged_list = []

    while left_half and right_half:
        if left_half[-1] <= right_half[-1]:
            merged_list.append(left_half.pop())
        else:
            merged_list.append(right_half.pop())
            total_inversions += len(left_half)

    merged_list.reverse()
    combined_list = right_half + left_half + merged_list
    total_inversions += left_inversions + right_inversions

    return combined_list, total_inversions

def count_total_inversions(array):
    _, inversion_count = merge_and_count_inversions(array)
    return inversion_count

def main():
    _ = input()  # Ignore the length input as it is not needed
    integer_array = list(map(int, input().split()))
    print(count_total_inversions(integer_array))

if __name__ == '__main__':
    main()