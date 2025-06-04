number_of_integers = int(input())

list_of_integers = [int(integer_string) for integer_string in input().split()]

list_of_integers.sort()

middle_index = number_of_integers // 2

difference_between_middle_elements = list_of_integers[middle_index] - list_of_integers[middle_index - 1]

print(difference_between_middle_elements)