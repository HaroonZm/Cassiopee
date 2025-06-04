def compute_triplet_sequence(count):
    previous_three = 0
    previous_two = 0
    previous_one = 0

    for iteration in range(count):
        new_value = (previous_three + previous_two + previous_one + 1) % 100000007
        previous_three, previous_two, previous_one = new_value, previous_three, previous_two

    return previous_three



def compute_quintuplet_sequence(count):
    fifth_previous = 0
    fourth_previous = 0
    third_previous = 0
    second_previous = 0
    first_previous = 0

    for iteration in range(count):
        new_value = (fifth_previous + fourth_previous + third_previous + second_previous + first_previous + 1) % 100000007
        fifth_previous, fourth_previous, third_previous, second_previous, first_previous = new_value, fifth_previous, fourth_previous, third_previous, second_previous

    return fifth_previous



while True:

    input_string = input()

    if input_string == "#":
        break

    result = 1
    previous_character = "_"
    consecutive_count = 1

    for current_character in input_string + "_":
        if current_character == previous_character:
            consecutive_count += 1

        else:
            if previous_character in "80":
                result = result * compute_triplet_sequence(consecutive_count) % 100000007
            else:
                result = result * compute_quintuplet_sequence(consecutive_count) % 100000007

            previous_character = current_character
            consecutive_count = 1

    print(result)