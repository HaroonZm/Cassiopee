maximum_seven_five_three_number = int(input())

list_of_seven_five_three_digits = [3, 5, 7]

count_of_valid_numbers = 0

if maximum_seven_five_three_number < 357:
    print(0)
    exit()


def generate_and_count_753_numbers(current_number_string):
    global count_of_valid_numbers

    next_number_string_with_three = str(current_number_string) + '3'
    next_number_string_with_five = str(current_number_string) + '5'
    next_number_string_with_seven = str(current_number_string) + '7'

    # Process the number ending with '3'
    if int(next_number_string_with_three) > maximum_seven_five_three_number:
        return
    if (
        '3' in str(next_number_string_with_three)
        and '5' in str(next_number_string_with_three)
        and '7' in str(next_number_string_with_three)
    ):
        count_of_valid_numbers += 1
    generate_and_count_753_numbers(next_number_string_with_three)

    # Process the number ending with '5'
    if int(next_number_string_with_five) > maximum_seven_five_three_number:
        return
    if (
        '3' in str(next_number_string_with_five)
        and '5' in str(next_number_string_with_five)
        and '7' in str(next_number_string_with_five)
    ):
        count_of_valid_numbers += 1
    generate_and_count_753_numbers(next_number_string_with_five)

    # Process the number ending with '7'
    if int(next_number_string_with_seven) > maximum_seven_five_three_number:
        return
    if (
        '3' in str(next_number_string_with_seven)
        and '5' in str(next_number_string_with_seven)
        and '7' in str(next_number_string_with_seven)
    ):
        count_of_valid_numbers += 1
    generate_and_count_753_numbers(next_number_string_with_seven)


generate_and_count_753_numbers('')

print(count_of_valid_numbers)