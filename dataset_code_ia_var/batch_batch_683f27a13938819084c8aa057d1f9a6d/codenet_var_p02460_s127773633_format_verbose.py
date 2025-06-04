if __name__ == '__main__':

    number_of_commands = int(input())
    key_value_dictionary = {}

    for command_index in range(number_of_commands):

        command_parts = input().split()
        command_type = command_parts[0]

        if command_type == "0":
            key_to_insert = command_parts[1]
            value_to_insert = command_parts[2]
            key_value_dictionary[key_to_insert] = value_to_insert

        elif command_type == "1":
            key_to_query = command_parts[1]
            if key_to_query in key_value_dictionary:
                print(key_value_dictionary[key_to_query])
            else:
                print("0")

        else:
            key_to_delete = command_parts[1]
            if key_to_delete in key_value_dictionary:
                del key_value_dictionary[key_to_delete]