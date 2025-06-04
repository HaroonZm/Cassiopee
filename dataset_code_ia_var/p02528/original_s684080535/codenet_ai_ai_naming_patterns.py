def bubble_sort_list(data_list, list_length):
    is_sorted = False
    current_pass = 0

    while not is_sorted:
        is_sorted = True
        for current_index in range(1, list_length - current_pass):
            if data_list[current_index] < data_list[current_index - 1]:
                data_list[current_index], data_list[current_index - 1] = data_list[current_index - 1], data_list[current_index]
                is_sorted = False
        current_pass += 1

input_list_length = int(raw_input())
input_data_list = map(int, raw_input().split())

bubble_sort_list(input_data_list, input_list_length)

print " ".join([str(element) for element in input_data_list])