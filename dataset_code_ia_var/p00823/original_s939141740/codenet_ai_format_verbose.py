def parse_expression():
    global current_position_in_expression
    global expression_char_list

    numeric_result = parse_term()

    while len(expression_char_list) > current_position_in_expression:
        if expression_char_list[current_position_in_expression] == '+':
            current_position_in_expression += 1
            numeric_result += parse_term()
        else:
            break

    return numeric_result

def parse_term():
    global current_position_in_expression
    global expression_char_list

    term_result = parse_factor()

    while len(expression_char_list) > current_position_in_expression:
        if expression_char_list[current_position_in_expression] == '*':
            current_position_in_expression += 1
            term_result *= parse_factor()
        else:
            break

    return term_result

def parse_factor():
    global current_position_in_expression
    global expression_char_list

    factor_result = 0

    if len(expression_char_list) > current_position_in_expression and expression_char_list[current_position_in_expression] == '(':
        current_position_in_expression += 1
        factor_result = parse_expression()
        current_position_in_expression += 1
    else:
        return parse_number()

    return factor_result

def parse_number():
    global current_position_in_expression
    global expression_char_list
    global variable_dictionary
    global successful_parsing

    numeric_value = 0

    if expression_char_list[current_position_in_expression].isdigit():
        while len(expression_char_list) > current_position_in_expression and expression_char_list[current_position_in_expression].isdigit():
            numeric_value *= 10
            numeric_value += int(expression_char_list[current_position_in_expression])
            current_position_in_expression += 1

    elif expression_char_list[current_position_in_expression] != '(' and expression_char_list[current_position_in_expression] != ')':
        variable_name = ''
        while (len(expression_char_list) > current_position_in_expression and 
               expression_char_list[current_position_in_expression] != '(' and 
               expression_char_list[current_position_in_expression] != ')' and 
               expression_char_list[current_position_in_expression] != '+' and 
               expression_char_list[current_position_in_expression] != '*'):
            variable_name += expression_char_list[current_position_in_expression]
            current_position_in_expression += 1
        if variable_name in variable_dictionary:
            numeric_value = int(variable_dictionary[variable_name])
        else:
            successful_parsing = False

    return numeric_value

def preprocess_expression():
    global expression_char_list

    expression_char_list = list(expression_char_list)
    current_index = 1

    while True:
        if current_index >= len(expression_char_list):
            break

        if expression_char_list[current_index].isdigit():
            expression_char_list.insert(current_index, '*')
            current_index += 1
            while current_index + 1 < len(expression_char_list) and expression_char_list[current_index + 1].isdigit():
                current_index += 1

        elif (expression_char_list[current_index] == '(' or expression_char_list[current_index].isupper()) and (expression_char_list[current_index - 1] != '('):
            expression_char_list.insert(current_index, '+')
            current_index += 1

        current_index += 1

    expression_char_list = ''.join(expression_char_list)

variable_dictionary = {}

while True:
    input_line = input()
    if input_line == 'END_OF_FIRST_PART':
        break

    variable_key, variable_value = input_line.split()
    variable_dictionary[variable_key] = variable_value

while True:
    expression_char_list = input()
    if expression_char_list == '0':
        break

    current_position_in_expression = 0
    successful_parsing = True

    preprocess_expression()
    result_of_evaluation = parse_expression()

    if successful_parsing:
        print(result_of_evaluation)
    else:
        print('UNKNOWN')