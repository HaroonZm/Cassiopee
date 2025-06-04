number_of_cats = 101

cat_entry_status = [0 for cat_index in range(number_of_cats)]

cat_stack = []

total_instructions = int(input())

cat_instruction_list = [int(instruction) for instruction in input().split()]

first_invalid_instruction = -1

for instruction_index in range(total_instructions):

    current_instruction = cat_instruction_list[instruction_index]

    if current_instruction > 0:

        cat_id_to_enter = current_instruction

        if cat_entry_status[cat_id_to_enter] == 1:
            first_invalid_instruction = instruction_index + 1
            break
        else:
            cat_entry_status[cat_id_to_enter] = 1
            cat_stack.append(cat_id_to_enter)

    else:

        cat_id_to_exit = -current_instruction

        if cat_entry_status[cat_id_to_exit] == 0:
            first_invalid_instruction = instruction_index + 1
            break
        else:
            cat_entry_status[cat_id_to_exit] = 0

            last_cat_in_stack = cat_stack.pop()

            if last_cat_in_stack != cat_id_to_exit:
                first_invalid_instruction = instruction_index + 1
                break

if first_invalid_instruction < 0:
    print("OK")
else:
    print(first_invalid_instruction)