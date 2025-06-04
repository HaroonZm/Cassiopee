NUMBER_OF_DIGITS = 20

cumulative_string_lengths = [0] * NUMBER_OF_DIGITS

from math import log10

for digit_count in xrange(1, NUMBER_OF_DIGITS):

    lower_bound = 10 ** (digit_count - 1) - 1
    upper_bound = 10 ** digit_count - 1

    fizzbuzz_length = (4 - digit_count) * (upper_bound / 3 + upper_bound / 5 - (upper_bound / 15) * 2 - lower_bound / 3 - lower_bound / 5 + (lower_bound / 15) * 2)
    buzz_length = (8 - digit_count) * (upper_bound / 15 - lower_bound / 15)
    number_length = digit_count * (upper_bound - lower_bound)

    cumulative_string_lengths[digit_count] = (
        cumulative_string_lengths[digit_count - 1] +
        fizzbuzz_length +
        buzz_length +
        number_length
    )


def compute_total_length_upto(m):

    if m == 0:
        return 0

    digit_length = int(log10(m)) + 1

    lower_bound = 10 ** (digit_length - 1) - 1
    upper_bound = m

    fizzbuzz_length = (4 - digit_length) * (upper_bound / 3 + upper_bound / 5 - (upper_bound / 15) * 2 - lower_bound / 3 - lower_bound / 5 + (lower_bound / 15) * 2)
    buzz_length = (8 - digit_length) * (upper_bound / 15 - lower_bound / 15)
    number_length = digit_length * (upper_bound - lower_bound)

    return (
        cumulative_string_lengths[digit_length - 1] +
        fizzbuzz_length +
        buzz_length +
        number_length
    )


input_length = input()
total_strings_to_skip = input_length

search_left = 0
search_right = 10 ** 18

while search_left + 1 < search_right:

    search_middle = (search_left + search_right) / 2

    if compute_total_length_upto(search_middle) <= total_strings_to_skip - 1:
        search_left = search_middle
    else:
        search_right = search_middle

index_of_current_string = compute_total_length_upto(search_left)
current_number = search_left + 1
generated_string = ""

while len(generated_string) < total_strings_to_skip - index_of_current_string + 20:

    if current_number % 15 == 0:
        generated_string += "FizzBuzz"
    elif current_number % 3 == 0:
        generated_string += "Fizz"
    elif current_number % 5 == 0:
        generated_string += "Buzz"
    else:
        generated_string += str(current_number)

    current_number += 1

print generated_string[total_strings_to_skip - index_of_current_string - 1 : total_strings_to_skip - index_of_current_string + 19]