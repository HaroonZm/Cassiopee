number_of_elements, window_size = map(int, input().split())

list_of_integers = list(map(int, input().split()))

product_dummy_variable = 1  # Not used, but kept as in original code

temporary_list = []

for current_index in range(len(list_of_integers) - window_size):

    current_element = list_of_integers[current_index]

    future_element = list_of_integers[current_index + window_size]

    if current_element < future_element:
        print("Yes")

    else:
        print("No")