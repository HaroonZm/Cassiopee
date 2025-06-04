def insertion_sort_and_display_steps(list_of_numbers):

    print(" ".join(map(str, list_of_numbers)))

    for current_index in range(1, len(list_of_numbers)):

        current_value_to_insert = list_of_numbers[current_index]
        position_to_compare = current_index - 1

        while (
            position_to_compare >= 0 and
            list_of_numbers[position_to_compare] > current_value_to_insert
        ):
            list_of_numbers[position_to_compare + 1] = list_of_numbers[position_to_compare]
            position_to_compare -= 1

        list_of_numbers[position_to_compare + 1] = current_value_to_insert

        print(" ".join(map(str, list_of_numbers)))


number_of_elements = int(raw_input())

user_input_numbers = map(int, raw_input().split())

insertion_sort_and_display_steps(user_input_numbers)