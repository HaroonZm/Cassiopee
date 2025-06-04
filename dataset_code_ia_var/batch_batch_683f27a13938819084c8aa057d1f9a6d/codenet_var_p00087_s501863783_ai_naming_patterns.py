import sys

stack = []
for input_line in sys.stdin:
    tokens = input_line.split()
    stack.clear()
    for token_index in range(len(tokens)):
        token = tokens[token_index]
        if token in ['+', '-', '*', '/']:
            operand_right = stack.pop()
            operand_left = stack.pop()
            if token == '+':
                result = operand_left + operand_right
            elif token == '-':
                result = operand_left - operand_right
            elif token == '*':
                result = operand_left * operand_right
            else:
                result = 1.0 * operand_left / operand_right
            stack.append(result)
        else:
            stack.append(float(token))
    print(stack[0])