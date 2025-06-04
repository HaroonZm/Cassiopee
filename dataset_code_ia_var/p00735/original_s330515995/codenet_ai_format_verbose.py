import math

maximum_number = 300000

is_eligible_number = [False] * (maximum_number + 1)

for current_number in range(1, maximum_number):

    remainder_when_divided_by_7 = current_number % 7

    if remainder_when_divided_by_7 == 6 or remainder_when_divided_by_7 == 1:

        is_eligible_number[current_number] = True

for potential_prime_candidate in range(2, int(math.sqrt(maximum_number))):

    if is_eligible_number[potential_prime_candidate] is True:

        multiplier = 2

        while potential_prime_candidate * multiplier <= maximum_number:

            is_eligible_number[potential_prime_candidate * multiplier] = False

            multiplier += 1

filtered_numbers_list = [
    index for index in range(len(is_eligible_number))
    if is_eligible_number[index] is True
]

while True:

    user_input_string = input()

    try:
        user_input_number = int(user_input_string)
    except ValueError:
        continue

    if user_input_number == 1:
        break

    divisors_list = [
        str(number)
        for number in filtered_numbers_list[1:]
        if user_input_number % number == 0
    ]

    print(
        "%d: %s" % (
            user_input_number,
            " ".join(divisors_list)
        )
    )