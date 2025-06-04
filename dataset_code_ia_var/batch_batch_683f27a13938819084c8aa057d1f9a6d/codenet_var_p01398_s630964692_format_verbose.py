while True:

    number_of_swaps = int(input())

    if number_of_swaps == 0:
        break

    original_message = input()
    numeric_message_list = [ord(character) - ord('a') for character in original_message]

    swap_indices_list = []

    for swap_input_index in range(number_of_swaps):
        swap_pair = tuple(map(int, input().split()))
        swap_indices_list.append(swap_pair)

    swap_indices_list.reverse()

    for swap_start_index, swap_end_index in swap_indices_list:
        swap_start_position = swap_start_index - 1
        swap_end_position = swap_end_index - 1

        difference = swap_end_position - swap_start_position

        new_value_at_end = (numeric_message_list[swap_start_position] + difference) % 26
        new_value_at_start = (numeric_message_list[swap_end_position] + difference) % 26

        numeric_message_list[swap_end_position] = new_value_at_end
        numeric_message_list[swap_start_position] = new_value_at_start

    decoded_message_list = [chr(numeric_value + ord('a')) for numeric_value in numeric_message_list]
    decoded_message = ''.join(decoded_message_list)

    print(decoded_message)