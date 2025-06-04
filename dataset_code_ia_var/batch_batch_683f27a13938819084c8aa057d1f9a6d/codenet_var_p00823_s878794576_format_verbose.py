element_weights = {}

def calculate_expression(expression):

    total_weight = 0

    current_index = 0

    expression_length = len(expression)

    while current_index < expression_length:

        current_character = expression[current_index]

        if current_character == "(":
            nested_expression = ""
            parenthesis_depth = 1
            current_index += 1

            while current_index < expression_length and parenthesis_depth > 0:
                nested_character = expression[current_index]

                if nested_character == "(":
                    parenthesis_depth += 1
                elif nested_character == ")":
                    parenthesis_depth -= 1

                if parenthesis_depth == 0:
                    break

                nested_expression += nested_character
                current_index += 1

            if parenthesis_depth > 0:
                raise SyntaxError("invalid syntax: unmatched parenthesis")

            group_weight = calculate_expression(nested_expression)

        elif "A" <= current_character <= "Z":
            element_symbol = current_character

            if (current_index + 1 < expression_length 
                and "a" <= expression[current_index + 1] <= "z"):
                element_symbol += expression[current_index + 1]
                current_index += 1

            group_weight = element_weights[element_symbol]

        else:
            raise SyntaxError("invalid syntax: unexpected character '%s'" % current_character)

        if (current_index + 1 < expression_length 
            and "1" <= expression[current_index + 1] <= "9"):

            multiplier_str = expression[current_index + 1]
            current_index += 1

            if (current_index + 1 < expression_length 
                and "0" <= expression[current_index + 1] <= "9"):
                multiplier_str += expression[current_index + 1]
                current_index += 1

            multiplier = int(multiplier_str)
        else:
            multiplier = 1

        total_weight += group_weight * multiplier
        current_index += 1

    return total_weight

# Input phase for the first part (element and their weights)
while True:

    input_line = raw_input()

    if input_line == "END_OF_FIRST_PART":
        break

    symbol_name, atomic_weight = input_line.split()

    element_weights[symbol_name] = int(atomic_weight)

# Input phase for the second part (expressions to evaluate)
while True:

    formula_line = raw_input()

    if formula_line == "0":
        break

    try:
        print calculate_expression(formula_line)
    except KeyError:
        print "UNKNOWN"