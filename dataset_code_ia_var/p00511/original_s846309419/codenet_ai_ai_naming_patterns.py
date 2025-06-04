current_value = int(input())
while True:
    operation_input = input()
    if operation_input == '+':
        operand_value = int(input())
        current_value += operand_value
    elif operation_input == '-':
        operand_value = int(input())
        current_value -= operand_value
    elif operation_input == '*':
        operand_value = int(input())
        current_value *= operand_value
    elif operation_input == '/':
        operand_value = int(input())
        current_value //= operand_value
    elif operation_input == '=':
        print(current_value)
        exit()