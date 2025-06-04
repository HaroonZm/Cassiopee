first_set_size = input()

first_integer_set = set(map(int, input().split()))

second_set_size = input()

second_integer_set = set(map(int, input().split()))

unique_elements_in_first_set = first_integer_set.difference(second_integer_set)

for unique_element in sorted(unique_elements_in_first_set):
    print(unique_element)