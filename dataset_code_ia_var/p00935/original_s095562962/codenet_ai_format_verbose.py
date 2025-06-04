def concatenate_strings(string_list):
    return ''.join(string_list)

number_of_inputs = int(input())

concatenated_digits = concatenate_strings(
    ''.join(input().split()) for _ in range(number_of_inputs // 19 + (number_of_inputs % 19 != 0))
)

current_number = 0

while True:
    if concatenated_digits.find(str(current_number)) == -1:
        print(current_number)
        exit()
    current_number += 1