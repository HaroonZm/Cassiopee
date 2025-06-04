import time
from itertools import product

def is_valid_expression(expression_string):
    # Check for invalid substrings representing illegal operator/parentheses usage
    invalid_substrings = ['(+', '(-', '(*', '++', '+-', '-+', '--', '**', '*+', '*-']
    for invalid_substring in invalid_substrings:
        if invalid_substring in expression_string:
            return False

    # Check for validity of parentheses usage with operators inside parentheses
    if '(' in expression_string or ')' in expression_string:
        parenthesis_depth_count = {}  # Key: Parenthesis depth, Value: operator count inside parentheses
        current_depth = -1
        for character in expression_string:
            if character == '(':
                current_depth += 1
                parenthesis_depth_count[current_depth] = 0
            elif character == ')':
                if parenthesis_depth_count.get(current_depth, 0) == 0:
                    return False
                current_depth -= 1
            elif character in '+-*' and current_depth in parenthesis_depth_count:
                parenthesis_depth_count[current_depth] += 1
        return True
    else:
        return True

def evaluate_expression_with_binary_numbers(expression_string):
    current_index = 0
    decimal_expression_builder = ''
    binary_number_characters = []

    try:
        while current_index < len(expression_string):
            current_character = expression_string[current_index]
            if current_character in '01':
                binary_number_characters.append(current_character)
            else:
                if binary_number_characters:
                    binary_number_as_string = ''.join(binary_number_characters)
                    binary_number_decimal_string = str(int(binary_number_as_string, 2))
                    if int(binary_number_decimal_string) >= 1024:
                        return -99999999
                    decimal_expression_builder += binary_number_decimal_string
                    binary_number_characters = []
                decimal_expression_builder += current_character
            current_index += 1

        if binary_number_characters:
            binary_number_as_string = ''.join(binary_number_characters)
            binary_number_decimal_string = str(int(binary_number_as_string, 2))
            decimal_expression_builder += binary_number_decimal_string

    except:
        return -99999999

    try:
        if is_valid_expression(decimal_expression_builder):
            evaluated_result = eval(decimal_expression_builder)
            if '-' not in decimal_expression_builder and evaluated_result < 1024:
                return evaluated_result
            elif '-' in decimal_expression_builder and evaluated_result < 1024:
                for operator_index in range(len(decimal_expression_builder)):
                    if decimal_expression_builder[operator_index] == '-':
                        minus_operator_position = operator_index
                        left_pointer = minus_operator_position - 1
                        right_pointer = minus_operator_position + 1

                        # Find the left operand, handling nested parentheses
                        parenthesis_balance = 0
                        while left_pointer >= 0:
                            if decimal_expression_builder[left_pointer] == ')':
                                parenthesis_balance += 1
                            elif decimal_expression_builder[left_pointer] == '(':
                                parenthesis_balance -= 1
                                if parenthesis_balance < 0:
                                    left_pointer += 1
                                    break
                            if parenthesis_balance == 0 and decimal_expression_builder[left_pointer] in '+-':
                                left_pointer += 1
                                break
                            left_pointer -= 1
                        left_pointer = max(left_pointer, 0)

                        # Find the right operand, handling nested parentheses
                        parenthesis_balance = 0
                        while right_pointer < len(decimal_expression_builder):
                            if decimal_expression_builder[right_pointer] == '(':
                                parenthesis_balance += 1
                            elif decimal_expression_builder[right_pointer] == ')':
                                parenthesis_balance -= 1
                                if parenthesis_balance < 0:
                                    break
                            if parenthesis_balance == 0 and decimal_expression_builder[right_pointer] in '+-':
                                break
                            right_pointer += 1

                        left_operand = eval(decimal_expression_builder[left_pointer:minus_operator_position])
                        right_operand = eval(decimal_expression_builder[minus_operator_position + 1:right_pointer])
                        if left_operand >= 1024 or right_operand >= 1024 or left_operand - right_operand < 0:
                            return -99999999
                return evaluated_result
            else:
                return -99999999
        else:
            return -99999999
    except:
        return -99999999

raw_input_segments = input().split('.')
maximum_result = -1
all_possible_operators = product('01+-*()', repeat=len(raw_input_segments) - 1)

for operator_combination in all_possible_operators:
    candidate_expression = raw_input_segments[0]
    next_segment_index = 1

    for operator_character in operator_combination:
        candidate_expression += operator_character + raw_input_segments[next_segment_index]
        next_segment_index += 1

    maximum_result = max(maximum_result, evaluate_expression_with_binary_numbers(candidate_expression))

print(maximum_result)