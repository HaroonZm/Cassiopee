while True:
    operand_left, operator, operand_right = map(str, input().split())
    if operator == '?':
        break

    if operator == '+':
        result = int(operand_left) + int(operand_right)
    elif operator == '-':
        result = int(operand_left) - int(operand_right)
    elif operator == '*':
        result = int(operand_left) * int(operand_right)
    elif operator == '/':
        result = int(operand_left) // int(operand_right)
    else:
        continue

    print(result)