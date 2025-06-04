number_of_elements = int(input())

string_elements_list = input().split()

final_result = 1

for possible_period_length in range(1, number_of_elements + 1):

    if number_of_elements % possible_period_length != 0:
        continue

    found_difference = False

    for current_index in range(number_of_elements - possible_period_length):

        if string_elements_list[current_index] == string_elements_list[current_index + possible_period_length]:
            continue

        found_difference = True
        break

    if found_difference:
        continue

    final_result = number_of_elements // possible_period_length
    break

print(final_result)