def main():

    presence_dictionary = {}

    number_of_inputs = int(raw_input())

    current_input_count = 0

    while current_input_count < number_of_inputs:

        user_command, user_key = raw_input().split(' ')

        is_insert_command = user_command[0] == 'i'

        if is_insert_command:
            presence_dictionary[user_key] = True

        else:
            if user_key in presence_dictionary:
                print 'yes'
            else:
                print 'no'

        current_input_count += 1

if __name__ == '__main__':
    main()