value_accumulator = input()
while True:
    try:
        operation_input = raw_input()
        if operation_input == '=':
            print value_accumulator
            break
        operand_value = input()
        if operation_input == '+':
            value_accumulator += operand_value
        elif operation_input == '-':
            value_accumulator -= operand_value
        elif operation_input == '*':
            value_accumulator *= operand_value
        elif operation_input == '/':
            value_accumulator /= operand_value
    except EOFError:
        break