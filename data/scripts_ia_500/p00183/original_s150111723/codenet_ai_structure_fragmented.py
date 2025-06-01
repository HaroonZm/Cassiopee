def read_input():
    return input()

def is_termination(input_data):
    return input_data == "0"

def all_chars_equal_and_not_plus(s):
    return s[0] != "+" and s[0] == s[1] == s[2]

def check_row(input_data):
    if all_chars_equal_and_not_plus(input_data):
        return input_data[0]
    return None

def check_column(inputs, index):
    if inputs[0][index] != "+" and inputs[0][index] == inputs[1][index] == inputs[2][index]:
        return inputs[0][index]
    return None

def check_diagonal(inputs, indices):
    if inputs[0][indices[0]] != "+" and inputs[0][indices[0]] == inputs[1][indices[1]] == inputs[2][indices[2]]:
        return inputs[0][indices[0]]
    return None

def process_inputs(input1, input2, input3):
    inputs = [input1, input2, input3]

    for i in range(3):
        result = check_row(inputs[i])
        if result is not None:
            return result

    for i in range(3):
        result = check_column(inputs, i)
        if result is not None:
            return result

    result = check_diagonal(inputs, (0, 1, 2))
    if result is not None:
        return result

    result = check_diagonal(inputs, (2, 1, 0))
    if result is not None:
        return result

    return "NA"

def main_loop():
    while True:
        input_data1 = read_input()
        if is_termination(input_data1):
            break
        input_data2 = read_input()
        input_data3 = read_input()

        output = process_inputs(input_data1, input_data2, input_data3)
        print(output)

main_loop()