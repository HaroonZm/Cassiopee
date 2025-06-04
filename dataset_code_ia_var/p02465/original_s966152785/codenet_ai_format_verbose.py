number_of_elements_set_a = int(input())

elements_set_a = {int(element) for element in input().split()}

number_of_elements_set_b = int(input())

elements_set_b = {int(element) for element in input().split()}

unique_elements_in_a = tuple(sorted(elements_set_a - elements_set_b))

for unique_element in unique_elements_in_a:
    print(unique_element)