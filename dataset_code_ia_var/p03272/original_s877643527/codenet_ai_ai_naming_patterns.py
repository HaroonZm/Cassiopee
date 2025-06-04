user_input = input()

user_input_parts = user_input.split()

part_one_int = int(user_input_parts[0])
part_two_int = int(user_input_parts[1])

result_value = part_one_int - part_two_int + 1

print(result_value)