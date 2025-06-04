number_of_statements = int(input())

statement_lines = [input().split() for statement_index in range(number_of_statements)]

statement_name_to_index = {}

for statement_index, statement_tokens in enumerate(statement_lines):
    statement_name_to_index[statement_tokens[0]] = statement_index

variable_name_to_index = {}

for statement_tokens in statement_lines:
    for operand in statement_tokens[2:]:
        if operand.isalpha() and operand not in variable_name_to_index:
            variable_name_to_index[operand] = len(variable_name_to_index)

variable_storage = [0] * len(variable_name_to_index)

def make_add_statement(destination_variable, left_operand, right_operand):

    dest_index = variable_name_to_index[destination_variable]

    if right_operand.isdigit():
        left_index = variable_name_to_index[left_operand]
        constant_value = int(right_operand)

        def execute_statement(program_counter):
            assert variable_storage[left_index] + constant_value < 16
            variable_storage[dest_index] = variable_storage[left_index] + constant_value
            return program_counter + 1

    else:
        left_index = variable_name_to_index[left_operand]
        right_index = variable_name_to_index[right_operand]

        def execute_statement(program_counter):
            assert variable_storage[left_index] + variable_storage[right_index] < 16
            variable_storage[dest_index] = variable_storage[left_index] + variable_storage[right_index]
            return program_counter + 1

    return execute_statement

def make_subtract_statement(destination_variable, left_operand, right_operand):

    dest_index = variable_name_to_index[destination_variable]

    if right_operand.isdigit():
        left_index = variable_name_to_index[left_operand]
        constant_value = int(right_operand)

        def execute_statement(program_counter):
            assert 0 <= variable_storage[left_index] - constant_value
            variable_storage[dest_index] = variable_storage[left_index] - constant_value
            return program_counter + 1

    else:
        left_index = variable_name_to_index[left_operand]
        right_index = variable_name_to_index[right_operand]

        def execute_statement(program_counter):
            assert 0 <= variable_storage[left_index] - variable_storage[right_index]
            variable_storage[dest_index] = variable_storage[left_index] - variable_storage[right_index]
            return program_counter + 1

    return execute_statement

def make_set_statement(destination_variable, value):

    dest_index = variable_name_to_index[destination_variable]

    if value.isdigit():
        constant_value = int(value)

        def execute_statement(program_counter):
            variable_storage[dest_index] = constant_value
            return program_counter + 1

    else:
        value_index = variable_name_to_index[value]

        def execute_statement(program_counter):
            variable_storage[dest_index] = variable_storage[value_index]
            return program_counter + 1

    return execute_statement

def make_conditional_jump_statement(condition_variable, target_statement_label):

    condition_index = variable_name_to_index[condition_variable]

    def execute_statement(program_counter):
        if variable_storage[condition_index]:
            return statement_name_to_index[target_statement_label]
        else:
            return program_counter + 1

    return execute_statement

def make_halt_statement():
    def execute_statement(program_counter):
        return number_of_statements
    return execute_statement

statement_execution_functions = []

for statement_index, statement_tokens in enumerate(statement_lines):
    statement_operation = statement_tokens[1]
    if statement_operation == 'ADD':
        statement_execution_functions.append(
            make_add_statement(*statement_tokens[2:])
        )
    elif statement_operation == 'SUB':
        statement_execution_functions.append(
            make_subtract_statement(*statement_tokens[2:])
        )
    elif statement_operation == 'SET':
        statement_execution_functions.append(
            make_set_statement(*statement_tokens[2:])
        )
    elif statement_operation == 'IF':
        statement_execution_functions.append(
            make_conditional_jump_statement(*statement_tokens[2:])
        )
    else:
        statement_execution_functions.append(
            make_halt_statement()
        )

program_result_is_finite = True

current_program_counter = 0

statement_execution_counts = [0] * number_of_statements

statement_execution_limit = 16 ** len(variable_name_to_index) + 10

try:
    while True:
        execute_current_statement = statement_execution_functions[current_program_counter]
        statement_execution_counts[current_program_counter] += 1

        if statement_execution_counts[current_program_counter] > statement_execution_limit:
            program_result_is_finite = False
            break

        current_program_counter = execute_current_statement(current_program_counter)

except Exception:
    pass

if program_result_is_finite:
    for variable_name in sorted(variable_name_to_index):
        print("%s=%d" % (variable_name, variable_storage[variable_name_to_index[variable_name]]))
else:
    print("inf")