user_input_strings = input().split(" ")

operand_stack = []

for current_token in user_input_strings:

    if current_token.isdigit():

        operand_stack.append(int(current_token))

    else:

        right_operand = operand_stack.pop()
        left_operand = operand_stack.pop()

        if current_token == '+':

            operand_stack.append(left_operand + right_operand)

        elif current_token == '-':

            operand_stack.append(left_operand - right_operand)

        elif current_token == '*':

            operand_stack.append(left_operand * right_operand)

result = operand_stack.pop()

print(result)