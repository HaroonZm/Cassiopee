if __name__ == "__main__":

    number_of_elements_in_list = int(input())

    integer_list = list(map(lambda user_input_element: int(user_input_element), input().split()))

    number_of_range_reverse_operations = int(input())

    for current_query_index in range(number_of_range_reverse_operations):

        range_start_index, range_end_index = map(lambda input_token: int(input_token), input().split())

        if range_start_index == 0:
            integer_list[range_start_index: range_end_index] = integer_list[range_end_index - 1:: -1]
        else:
            integer_list[range_start_index: range_end_index] = integer_list[range_end_index - 1: range_start_index - 1: -1]

    formatted_output_list = [str(current_element) for current_element in integer_list]

    print(" ".join(formatted_output_list))