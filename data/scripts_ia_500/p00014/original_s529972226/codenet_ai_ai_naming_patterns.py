import sys

START_INDEX = 0
END_INDEX = 600

def square_value(input_value):
    return input_value ** 2

if __name__ == '__main__':
    for input_line in sys.stdin:
        step_value = int(input_line)
        accumulated_sum = 0
        for current_index in range(START_INDEX, END_INDEX, step_value):
            accumulated_sum += step_value * square_value(current_index)
        print(accumulated_sum)