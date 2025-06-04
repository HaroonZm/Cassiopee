input_tokens = input().split()

operand_stack = []

for current_token in input_tokens:

    if current_token == '+':

        right_operand = operand_stack.pop()
        left_operand = operand_stack.pop()
        operand_stack.append(left_operand + right_operand)

    elif current_token == '-':

        right_operand = operand_stack.pop()
        left_operand = operand_stack.pop()
        operand_stack.append(left_operand - right_operand)

    elif current_token == '*':

        right_operand = operand_stack.pop()
        left_operand = operand_stack.pop()
        operand_stack.append(left_operand * right_operand)

    else:

        operand_stack.append(int(current_token))


print(operand_stack[-1])