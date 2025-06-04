while True:
    try:
        input_line = raw_input()
        operand_left, operand_right = map(int, input_line.split())
        result_difference = operand_left - operand_right
        print result_difference
    except:
        break