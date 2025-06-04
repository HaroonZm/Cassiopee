operators_functions = {
    "+": lambda first_operand, second_operand: second_operand + first_operand,
    "-": lambda first_operand, second_operand: second_operand - first_operand,
    "*": lambda first_operand, second_operand: second_operand * first_operand
}

operands_stack = []

user_input = input()

for token in user_input.split():

    if token in operators_functions:
        first_operand = operands_stack.pop()
        second_operand = operands_stack.pop()
        result = operators_functions[token](first_operand, second_operand)
        operands_stack.append(result)
    else:
        number = int(token)
        operands_stack.append(number)

print(operands_stack[-1])