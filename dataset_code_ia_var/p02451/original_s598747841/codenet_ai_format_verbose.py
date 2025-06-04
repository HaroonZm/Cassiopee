import bisect

number_of_elements = int(input())

sorted_integer_list = list(map(int, input().split()))

number_of_queries = int(input())

for query_index in range(number_of_queries):

    target_value = int(input())

    insertion_point = bisect.bisect(sorted_integer_list, target_value)

    element_exists = False
    if insertion_point - 1 >= 0 and sorted_integer_list[insertion_point - 1] == target_value:
        element_exists = True

    if element_exists:
        print(1)
    else:
        print(0)