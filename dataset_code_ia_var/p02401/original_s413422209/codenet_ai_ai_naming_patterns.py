while True:
    operand_left, operator_symbol, operand_right = input().split()
    operand_left = int(operand_left)
    operand_right = int(operand_right)

    if operator_symbol == "?":
        break
    elif operator_symbol == "+":
        print(operand_left + operand_right)
    elif operator_symbol == "-":
        print(operand_left - operand_right)
    elif operator_symbol == "*":
        print(operand_left * operand_right)
    else:
        print(operand_left // operand_right)