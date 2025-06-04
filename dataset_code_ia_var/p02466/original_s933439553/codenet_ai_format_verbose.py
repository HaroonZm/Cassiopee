number_of_elements_in_first_list = int(input())

first_integer_list = list(map(int, input().split()))

number_of_elements_in_second_list = int(input())

second_integer_list = list(map(int, input().split()))

symmetric_difference_set = set(first_integer_list) ^ set(second_integer_list)

symmetric_difference_list = list(symmetric_difference_set)

symmetric_difference_list.sort()

for unique_element in symmetric_difference_list:
    print(unique_element)