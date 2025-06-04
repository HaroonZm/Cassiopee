number_of_queries = int(input())

dictionary_of_values = {}

for query_index in range(number_of_queries):

    user_command = input().split()

    command_type = user_command[0]

    key = user_command[1]

    if command_type == "0":

        value_to_insert = int(user_command[2])

        dictionary_of_values[key] = value_to_insert

    elif command_type == "1":

        try:

            value_to_print = dictionary_of_values[key]

            print(value_to_print)

        except KeyError:

            print(0)

    else:

        try:

            del dictionary_of_values[key]

        except KeyError:

            pass