import sys

def compute_result(param_a, param_b):
    if param_a == 0 and param_b <= 99:
        return param_b
    if param_a == 1 and param_b <= 99:
        return 100 * param_b
    if param_a == 2 and param_b <= 99:
        return 10000 * param_b
    if param_a == 0:
        return 101
    if param_a == 1:
        return 10100
    return 1010000

def parse_input_line():
    input_line = sys.stdin.readline().rstrip()
    str_a, str_b = input_line.split(' ')
    int_a = int(str_a)
    int_b = int(str_b)
    return int_a, int_b

def run_program():
    input_a, input_b = parse_input_line()
    output_result = compute_result(input_a, input_b)
    print(output_result)

if __name__ == '__main__':
    run_program()