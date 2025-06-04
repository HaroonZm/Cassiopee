user_input_string = input()

character_list = []

for character_index in range(len(user_input_string)):
    character_list.append(user_input_string[character_index])

character_list.sort()

current_run_length = 1
even_pairs_judge = 1

if len(user_input_string) % 2 == 0:

    for scan_index in range(len(user_input_string) - 1):

        if character_list[current_run_length + scan_index] == character_list[current_run_length + scan_index - 1]:
            even_pairs_judge += 1
        else:
            if even_pairs_judge % 2 != 0:
                print("No")
                exit()
            else:
                even_pairs_judge = 1

        if scan_index == len(user_input_string) - 2:
            if even_pairs_judge % 2 == 0:
                print("Yes")
            else:
                print("No")
else:
    print("No")