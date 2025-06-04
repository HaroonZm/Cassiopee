number_of_elements_in_first_set = int(input())

first_set_elements = set(map(int, input().split()))

number_of_elements_in_second_set = int(input())

second_set_elements = set(map(int, input().split()))

symmetric_difference_set = first_set_elements ^ second_set_elements

if symmetric_difference_set:
    sorted_symmetric_difference = sorted(symmetric_difference_set)
    print(*sorted_symmetric_difference, sep='\n')