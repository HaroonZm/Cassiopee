while True:

    user_input_string, conversion_type = input().split()

    if conversion_type == 'X':
        break

    string_as_char_list = list(user_input_string)

    if ('_' in string_as_char_list) and (conversion_type == 'U' or conversion_type == 'L'):

        underscore_encountered = 0

        for current_index in range(len(string_as_char_list)):
            if current_index == 0 and conversion_type == 'U':
                string_as_char_list[current_index] = string_as_char_list[current_index].upper()
            elif string_as_char_list[current_index] == '_':
                underscore_encountered += 1
            elif underscore_encountered == 1:
                string_as_char_list[current_index] = string_as_char_list[current_index].upper()
                underscore_encountered = 0

        string_as_char_list = [char for char in string_as_char_list if char != '_']

    elif conversion_type == 'U':
        string_as_char_list[0] = string_as_char_list[0].upper()

    elif conversion_type == 'L':
        string_as_char_list[0] = string_as_char_list[0].lower()

    else:

        current_scan_position = 0

        for current_index in range(len(string_as_char_list)):

            if current_index == 0:
                string_as_char_list[0] = string_as_char_list[0].lower()
                current_scan_position += 1

            elif string_as_char_list[current_scan_position].isupper():
                string_as_char_list[current_scan_position] = string_as_char_list[current_scan_position].lower()
                string_as_char_list.insert(current_scan_position, '_')
                current_scan_position += 2

            else:
                current_scan_position += 1

    for output_index in range(len(string_as_char_list)):
        if output_index == len(string_as_char_list) - 1:
            print(string_as_char_list[output_index])
        else:
            print(string_as_char_list[output_index], end='')