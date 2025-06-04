import sys
from collections import defaultdict

def read_int_input():
    return int(sys.stdin.readline())

def read_int_list():
    return list(map(int, sys.stdin.readline().split()))

def read_string_as_list():
    return list(sys.stdin.readline())[:-1]

def function_F():
    def dfs_generate_expressions(current_index, current_expression):
        if current_index == len(input_expression_list):
            all_possible_expressions.append(current_expression)
        else:
            if input_expression_list[current_index] == ".":
                for bit_value in range(2):
                    dfs_generate_expressions(current_index + 1, current_expression + [str(bit_value)])
                for operator in "+-*()":
                    dfs_generate_expressions(current_index + 1, current_expression + [operator])
            else:
                dfs_generate_expressions(current_index + 1, current_expression + [input_expression_list[current_index]])

    def parse_expression(expression_list, start_index):
        if start_index == float("inf"):
            return -1, float("inf")
        opened_bracket = expression_list[start_index-1] == "("
        operation_count = 0
        term_value, next_index, operation_count = parse_term(expression_list, start_index, operation_count)
        while next_index < len(expression_list) and expression_list[next_index] in "+-":
            operation_count += 1
            operator, next_index = read_operator(expression_list, next_index)
            next_term, next_index, operation_count = parse_term(expression_list, next_index, operation_count)
            term_value = calculate(operator, term_value, next_term)
            if term_value >= 1024 or term_value < 0:
                return -1, float("inf")
        if opened_bracket and not operation_count:
            return -1, float("inf")
        return term_value, next_index

    def parse_term(expression_list, current_index, operation_count):
        factor_value, next_index = parse_factor(expression_list, current_index)
        while next_index < len(expression_list) and expression_list[next_index] == "*":
            operation_count += 1
            operator, next_index = read_operator(expression_list, next_index)
            next_factor, next_index = parse_factor(expression_list, next_index)
            factor_value = calculate(operator, factor_value, next_factor)
            if factor_value >= 1024 or factor_value < 0:
                return -1, float("inf"), operation_count
        return factor_value, next_index, operation_count

    def read_operator(expression_list, current_index):
        return expression_list[current_index], current_index + 1

    def parse_factor(expression_list, current_index):
        if current_index >= len(expression_list):
            return -1, float("inf")
        if expression_list[current_index] == "(":
            current_index += 1
            value_inside_brackets, current_index = parse_expression(expression_list, current_index)
            if current_index >= len(expression_list) or expression_list[current_index] != ")":
                return -1, float("inf")
            current_index += 1
            return value_inside_brackets, current_index
        else:
            if not expression_list[current_index].isdecimal():
                return -1, float("inf")
            numeric_value = int(expression_list[current_index])
            current_index += 1
            while current_index < len(expression_list) and expression_list[current_index].isdecimal():
                numeric_value *= 2
                numeric_value += int(expression_list[current_index])
                current_index += 1
            if numeric_value >= 1024 or numeric_value < 0:
                return -1, float("inf")
            return numeric_value, current_index

    def calculate(operator, left_operand, right_operand):
        if operator == "+":
            return left_operand + right_operand
        elif operator == "-":
            return left_operand - right_operand
        elif operator == "*":
            return left_operand * right_operand

    input_expression_list = read_string_as_list()
    possible_digit_count = defaultdict(int)
    for possible_digit in range(2):
        possible_digit_count[str(possible_digit)] += 1
    all_possible_expressions = []
    dfs_generate_expressions(0, [])
    maximum_valid_expression_value = -1
    for possible_expression in all_possible_expressions:
        expression_value, final_index = parse_expression(possible_expression, 0)
        if final_index == len(possible_expression):
            maximum_valid_expression_value = max(maximum_valid_expression_value, expression_value)
    print(maximum_valid_expression_value)
    return

if __name__ == "__main__":
    function_F()