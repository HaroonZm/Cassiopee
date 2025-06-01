import sys
from sys import stdin
input_line = stdin.readline

def main(arguments_list):
    while True:
        input_number = int(input_line())
        if input_number == 0:
            break

        step_counter = 0
        while input_number != 1:
            if input_number % 2 == 0:
                input_number //= 2
            else:
                input_number = input_number * 3 + 1
            step_counter += 1
        print(step_counter)

if __name__ == '__main__':
    main(sys.argv[1:])