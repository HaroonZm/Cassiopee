first_string_input = input()
second_string_input = input()

is_rotation_found = False

for rotation_index in range(len(first_string_input)):
    
    if first_string_input == second_string_input:
        is_rotation_found = True
        print("Yes")
        break

    first_string_input = first_string_input[-1] + first_string_input[:-1]

if not is_rotation_found:
    print("No")