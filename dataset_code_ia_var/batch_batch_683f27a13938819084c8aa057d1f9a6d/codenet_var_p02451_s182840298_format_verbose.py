number_of_elements = int(input())

sorted_integer_list = list(map(int, input().split(' ')))

def is_value_in_sorted_list(target_value):
    left_index = 0
    right_index = number_of_elements - 1

    while right_index - left_index >= 0:
        middle_index = int((left_index + right_index) / 2)

        middle_value = sorted_integer_list[middle_index]

        if middle_value == target_value:
            return 1

        if middle_value < target_value:
            left_index = middle_index + 1

        elif target_value < middle_value:
            right_index = middle_index - 1

    return 0

number_of_queries = int(input())

for query_index in range(number_of_queries):
    value_to_search = int(input())
    print(is_value_in_sorted_list(value_to_search))