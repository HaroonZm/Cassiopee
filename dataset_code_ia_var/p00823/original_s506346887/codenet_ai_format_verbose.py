from collections import defaultdict

variable_value_dictionary = defaultdict(int)

def evaluate_expression(expression_string, tokenize_input=1):
    is_outside_parentheses = True
    left_parenthesis_count = 0
    right_parenthesis_count = 0
    leftmost_parenthesis_index = float("INF")
    nested_expression_result = 0
    character_index = 0
    tokenized_expression = []

    if tokenize_input:
        while character_index < len(expression_string):
            if expression_string[character_index].isupper():
                variable_token = expression_string[character_index]
                character_index += 1
                while (character_index < len(expression_string) and 
                       expression_string[character_index].islower()):
                    variable_token += expression_string[character_index]
                    character_index += 1
                tokenized_expression.append(variable_token)

            elif expression_string[character_index].isdecimal():
                number_token = expression_string[character_index]
                character_index += 1
                while (character_index < len(expression_string) and 
                       expression_string[character_index].isdecimal()):
                    number_token += expression_string[character_index]
                    character_index += 1
                tokenized_expression.append(number_token)

            else:
                tokenized_expression.append(expression_string[character_index])
                character_index += 1
    else:
        tokenized_expression = expression_string

    expression_sequence = tokenized_expression
    computed_result = 0
    current_index = 0

    while current_index < len(expression_sequence):
        current_token = expression_sequence[current_index]

        if current_token == "(":
            is_outside_parentheses = False
            left_parenthesis_count += 1
            leftmost_parenthesis_index = min(leftmost_parenthesis_index, current_index)

        elif current_token == ")":
            right_parenthesis_count += 1

            if left_parenthesis_count == right_parenthesis_count:
                nested_expression_result = evaluate_expression(
                    expression_sequence[leftmost_parenthesis_index + 1 : current_index],
                    tokenize_input=0
                )

                if nested_expression_result == "UNKNOWN":
                    return "UNKNOWN"

                is_outside_parentheses = True

                if current_index != len(expression_sequence) - 1:
                    next_token = expression_sequence[current_index + 1]
                    if next_token.isdecimal():
                        current_index += 1
                        nested_expression_result *= int(next_token)
                
                computed_result += nested_expression_result
                leftmost_parenthesis_index = float("INF")
                left_parenthesis_count = 0
                right_parenthesis_count = 0

        else:
            if is_outside_parentheses:
                if current_token not in variable_value_dictionary.keys():
                    return "UNKNOWN"

                variable_token_value = variable_value_dictionary[current_token]

                if current_index != len(expression_sequence) - 1:
                    next_token = expression_sequence[current_index + 1]
                    if next_token.isdecimal():
                        current_index += 1
                        variable_token_value *= int(next_token)

                computed_result += variable_token_value

        current_index += 1

    return computed_result

if __name__ == "__main__":
    while True:
        variable_assignment_input = input()
        if variable_assignment_input == "END_OF_FIRST_PART":
            break
        variable_name, variable_value = variable_assignment_input.split()
        variable_value_dictionary[variable_name] = int(variable_value)

    while True:
        expression_input = input()
        if expression_input == "0":
            break
        print(evaluate_expression(expression_input))