prime_flag_array = [0 for index in range(300000)]

special_number_list = []

offsets_around_multiple_of_seven = [-1, 1]

for multiplier in range(1, int(300000 / 7) + 1):

    current_multiple_of_seven = 7 * multiplier

    for offset in offsets_around_multiple_of_seven:

        candidate_number = current_multiple_of_seven + offset

        if candidate_number < 300000 and prime_flag_array[candidate_number] == 0:

            special_number_list.append(candidate_number)

            for factor in range(2, int(300000 / 2)):

                if candidate_number * factor >= 300000:
                    break

                prime_flag_array[candidate_number * factor] = -1

while True:

    user_input_number = int(input())

    if user_input_number == 1:
        break

    divisible_special_numbers = [
        str(number)
        for number in special_number_list
        if number <= user_input_number and user_input_number % number == 0
    ]

    print(
        str(user_input_number) + ':',
        ' '.join(divisible_special_numbers)
    )