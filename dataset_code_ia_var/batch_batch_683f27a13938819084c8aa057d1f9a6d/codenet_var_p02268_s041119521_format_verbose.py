def count(common_elements_source_sorted, elements_to_check):
    """
    Returns the number of elements in elements_to_check that are also present in common_elements_source_sorted.

    - common_elements_source_sorted: a sequence (list) of integers, sorted in ascending order.
    - elements_to_check: a sequence (list) of unique integers.

    >>> count([1, 2, 3], [1, 3])
    2
    >>> count([1, 2, 3, 4, 5], [3, 4, 1])
    3
    >>> count([1, 2, 3], [5])
    0
    >>> count([1, 1, 2, 2, 3], [1, 2])
    2
    """

    def is_element_in_sorted_list(left_index, right_index, value_to_find):
        while left_index <= right_index:
            middle_index = (left_index + right_index) // 2

            if common_elements_source_sorted[middle_index] > value_to_find:
                right_index = middle_index - 1

            elif common_elements_source_sorted[middle_index] < value_to_find:
                left_index = middle_index + 1

            else:
                return True

        return False

    total_found = 0

    for element in elements_to_check:
        if is_element_in_sorted_list(0, len(common_elements_source_sorted) - 1, element):
            total_found += 1

    return total_found


def run():
    _ = input()  # First input ignored (usually list length)
    sorted_integer_list = [int(number) for number in input().split()]

    _ = input()  # Second input ignored (usually list length)
    integers_to_check = [int(number) for number in input().split()]

    print(count(sorted_integer_list, integers_to_check))


if __name__ == '__main__':
    run()