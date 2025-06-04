def evaluate_expression(input_string):
    token_list = input_string.split()
    operand_stack = []
    for token_index in range(len(token_list)):
        current_token = token_list[token_index]
        if current_token == "+":
            right_operand = operand_stack.pop()
            left_operand = operand_stack.pop()
            operand_stack.append(left_operand + right_operand)
        elif current_token == "-":
            right_operand = operand_stack.pop()
            left_operand = operand_stack.pop()
            operand_stack.append(left_operand - right_operand)
        elif current_token == "*":
            right_operand = operand_stack.pop()
            left_operand = operand_stack.pop()
            operand_stack.append(left_operand * right_operand)
        elif current_token == "/":
            right_operand = operand_stack.pop()
            left_operand = operand_stack.pop()
            operand_stack.append(left_operand / right_operand)
        else:
            operand_stack.append(float(current_token))
    return operand_stack[0]

while True:
    try:
        input_line = raw_input()
        print evaluate_expression(input_line)
    except:
        break