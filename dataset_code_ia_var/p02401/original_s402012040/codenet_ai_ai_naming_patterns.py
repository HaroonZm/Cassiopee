while True:
    operand_left_str, operator_str, operand_right_str = input().split()
    operand_left_int = int(operand_left_str)
    operand_right_int = int(operand_right_str)
    if operator_str == '?':
        break
    elif operator_str == '+':
        print(operand_left_int + operand_right_int)
    elif operator_str == '-':
        print(operand_left_int - operand_right_int)
    elif operator_str == '*':
        print(operand_left_int * operand_right_int)
    elif operator_str == '/':
        print(int(operand_left_int / operand_right_int))