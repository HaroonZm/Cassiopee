#!/usr/bin/env python3
# ITP2_6_A: Binary Search

from bisect import bisect

def element_exists_in_sorted_list(sorted_integer_list, target_value):
    """
    Returns True if target_value exists in sorted_integer_list, else False.
    Assumes sorted_integer_list is sorted in ascending order.

    >>> element_exists_in_sorted_list([1, 2, 3], 2)
    True
    >>> element_exists_in_sorted_list([1, 2, 3], 4)
    False
    >>> element_exists_in_sorted_list([1, 2, 3], 3)
    True
    >>> element_exists_in_sorted_list([1, 2, 3], 0)
    False
    >>> element_exists_in_sorted_list([1, 2, 3], 1)
    True
    """
    insertion_index = bisect(sorted_integer_list, target_value)
    is_within_bounds = 0 < insertion_index <= len(sorted_integer_list)
    if is_within_bounds and sorted_integer_list[insertion_index - 1] == target_value:
        return True
    else:
        return False

def main():
    number_of_elements = int(input())
    
    sorted_integer_list = [
        int(element) for element in input().split()
    ]
    assert number_of_elements == len(sorted_integer_list)
    
    number_of_queries = int(input())
    for _ in range(number_of_queries):
        query_value = int(input())
        if element_exists_in_sorted_list(sorted_integer_list, query_value):
            print(1)
        else:
            print(0)

if __name__ == '__main__':
    main()