while True:
    try:
        tokens_input = input()
        tokens_list = tokens_input.split()
    except EOFError:
        break

    eval_stack = []
    for token in tokens_list:
        if token == '+':
            operand_right = eval_stack.pop()
            operand_left = eval_stack.pop()
            result = operand_left + operand_right
            eval_stack.append(result)
        elif token == '-':
            operand_right = eval_stack.pop()
            operand_left = eval_stack.pop()
            result = operand_left - operand_right
            eval_stack.append(result)
        elif token == '*':
            operand_right = eval_stack.pop()
            operand_left = eval_stack.pop()
            result = operand_left * operand_right
            eval_stack.append(result)
        elif token == '/':
            operand_right = eval_stack.pop()
            operand_left = eval_stack.pop()
            result = operand_left / operand_right
            eval_stack.append(result)
        else:
            value = int(token)
            eval_stack.append(value)
    output_value = eval_stack[0]
    print("{:.8f}".format(output_value))