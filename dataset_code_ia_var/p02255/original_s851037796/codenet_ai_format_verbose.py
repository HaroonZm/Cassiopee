def insertion_sort_with_verbose_output(list_of_strings, number_of_elements):

    print(" ".join(list_of_strings))

    list_of_integers = list(map(int, list_of_strings))

    for current_index in range(1, number_of_elements):

        value_to_insert = list_of_integers[current_index]
        comparison_index = current_index - 1

        while (comparison_index >= 0 and 
               list_of_integers[comparison_index] > value_to_insert):

            list_of_integers[comparison_index + 1] = list_of_integers[comparison_index]
            comparison_index -= 1

        list_of_integers[comparison_index + 1] = value_to_insert

        stringified_list = list(map(str, list_of_integers))
        print(" ".join(stringified_list))

    return list_of_integers

number_of_elements_input = int(raw_input())
input_string_list = raw_input().split()
insertion_sort_with_verbose_output(input_string_list, number_of_elements_input)