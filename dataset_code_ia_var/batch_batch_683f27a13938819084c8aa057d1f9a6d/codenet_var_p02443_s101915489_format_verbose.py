number_of_elements = int(input())

elements_list = list(map(int, input().split()))

number_of_queries = int(input())

while number_of_queries > 0:
    number_of_queries -= 1

    left_index, right_index = map(int, input().split())

    # Reverse the sublist from left_index to right_index (exclusive)
    elements_list[left_index:right_index] = elements_list[left_index:right_index][::-1]

print(*elements_list)