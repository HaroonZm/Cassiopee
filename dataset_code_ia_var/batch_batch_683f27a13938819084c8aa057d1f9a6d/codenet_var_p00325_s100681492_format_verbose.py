from itertools import product

def analyze_program_termination():
    total_program_lines = int(input())
    parsed_program_lines = [input().split() for _ in range(total_program_lines)]

    variable_names_set = set()
    for program_line_tokens in parsed_program_lines:
        for token in program_line_tokens:
            if "a" <= token <= "z":
                variable_names_set.add(token)

    sorted_variable_names = sorted(list(variable_names_set))
    variable_values = [0] * len(sorted_variable_names)
    variable_name_to_index = {name: idx for idx, name in enumerate(sorted_variable_names)}

    label_name_to_line_index = {}
    for line_index, program_line_tokens in enumerate(parsed_program_lines):
        label_name_to_line_index[program_line_tokens[0]] = line_index

    def transform_instruction(instruction_tokens):
        instruction_type = instruction_tokens[1]

        if instruction_type == "ADD":
            target_variable = instruction_tokens[2]
            operand1 = instruction_tokens[3]
            operand2 = instruction_tokens[4]
            if operand2 in variable_name_to_index:
                return [0, variable_name_to_index[target_variable], variable_name_to_index[operand1], variable_name_to_index[operand2]]
            else:
                return [1, variable_name_to_index[target_variable], variable_name_to_index[operand1], int(operand2)]
        if instruction_type == "SUB":
            target_variable = instruction_tokens[2]
            operand1 = instruction_tokens[3]
            operand2 = instruction_tokens[4]
            if operand2 in variable_name_to_index:
                return [2, variable_name_to_index[target_variable], variable_name_to_index[operand1], variable_name_to_index[operand2]]
            else:
                return [3, variable_name_to_index[target_variable], variable_name_to_index[operand1], int(operand2)]
        if instruction_type == "SET":
            target_variable = instruction_tokens[2]
            value_or_variable = instruction_tokens[3]
            if value_or_variable in variable_name_to_index:
                return [4, variable_name_to_index[target_variable], variable_name_to_index[value_or_variable]]
            else:
                return [5, variable_name_to_index[target_variable], int(value_or_variable)]
        if instruction_type == "IF":
            condition_variable = instruction_tokens[2]
            jump_label = instruction_tokens[3]
            jump_line = label_name_to_line_index.get(jump_label, 100)
            return [6, variable_name_to_index[condition_variable], jump_line]
        if instruction_type == "HALT":
            return [7]

    program_instructions = [transform_instruction(line_tokens) for line_tokens in parsed_program_lines]

    number_of_variables = len(sorted_variable_names)
    total_possible_states = 16 ** number_of_variables
    state_and_line_already_visited = [[False] * total_program_lines for _ in range(total_possible_states)]

    variable_index_powers_of_16 = [1, 16, 256, 4096, 65536]

    current_line_index = 0
    current_state_hash = 0

    while True:
        if current_line_index >= total_program_lines:
            return True, sorted_variable_names, variable_values

        if state_and_line_already_visited[current_state_hash][current_line_index]:
            return False, sorted_variable_names, variable_values

        state_and_line_already_visited[current_state_hash][current_line_index] = True

        current_instruction = program_instructions[current_line_index]
        instruction_type = current_instruction[0]

        if instruction_type == 0:  # ADD with two variables
            target_idx, op1_idx, op2_idx = current_instruction[1:]
            addition_result = variable_values[op1_idx] + variable_values[op2_idx]
            if not addition_result < 16:
                return True, sorted_variable_names, variable_values
            current_state_hash += (addition_result - variable_values[target_idx]) * variable_index_powers_of_16[target_idx]
            variable_values[target_idx] = addition_result

        elif instruction_type == 1:  # ADD with constant
            target_idx, op1_idx, constant_operand = current_instruction[1:3] + [current_instruction[3]]
            addition_result = variable_values[op1_idx] + constant_operand
            if not addition_result < 16:
                return True, sorted_variable_names, variable_values
            current_state_hash += (addition_result - variable_values[target_idx]) * variable_index_powers_of_16[target_idx]
            variable_values[target_idx] = addition_result

        elif instruction_type == 2:  # SUB with two variables
            target_idx, op1_idx, op2_idx = current_instruction[1:]
            subtraction_result = variable_values[op1_idx] - variable_values[op2_idx]
            if not 0 <= subtraction_result:
                return True, sorted_variable_names, variable_values
            current_state_hash += (subtraction_result - variable_values[target_idx]) * variable_index_powers_of_16[target_idx]
            variable_values[target_idx] = subtraction_result

        elif instruction_type == 3:  # SUB with constant
            target_idx, op1_idx, constant_operand = current_instruction[1:3] + [current_instruction[3]]
            subtraction_result = variable_values[op1_idx] - constant_operand
            if not 0 <= subtraction_result:
                return True, sorted_variable_names, variable_values
            current_state_hash += (subtraction_result - variable_values[target_idx]) * variable_index_powers_of_16[target_idx]
            variable_values[target_idx] = subtraction_result

        elif instruction_type == 4:  # SET to another variable's value
            target_idx, source_idx = current_instruction[1:]
            current_state_hash += (variable_values[source_idx] - variable_values[target_idx]) * variable_index_powers_of_16[target_idx]
            variable_values[target_idx] = variable_values[source_idx]

        elif instruction_type == 5:  # SET to constant
            target_idx, constant_value = current_instruction[1:]
            current_state_hash += (constant_value - variable_values[target_idx]) * variable_index_powers_of_16[target_idx]
            variable_values[target_idx] = constant_value

        elif instruction_type == 6:  # IF and possibly jump
            condition_variable_idx = current_instruction[1]
            jump_destination_line = current_instruction[2]
            if variable_values[condition_variable_idx]:
                current_line_index = jump_destination_line - 1

        else:  # HALT instruction
            return True, sorted_variable_names, variable_values

        current_line_index += 1

termination_flag, variable_names_output, final_variable_values = analyze_program_termination()
if termination_flag:
    for variable_name, final_value in zip(variable_names_output, final_variable_values):
        print(f"{variable_name}={final_value}")
else:
    print("inf")