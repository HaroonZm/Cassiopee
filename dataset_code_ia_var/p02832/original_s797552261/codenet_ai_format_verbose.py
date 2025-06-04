import sys

input_read_entire = sys.stdin.read
input_read_line = sys.stdin.readline
input_read_lines = sys.stdin.readlines

sys.setrecursionlimit(10 ** 9)
INFINITE_DISTANCE = 1 << 60
MODULO_CONST = 1000000007

def main():
    input_values = list(map(int, input_read_entire().split()))
    sequence_length = input_values[0]
    sequence_numbers = input_values[1:]

    current_expected_number = 1

    for number in sequence_numbers:
        if number == current_expected_number:
            current_expected_number += 1

    if current_expected_number == 1:
        print(-1)
    else:
        min_removals_needed = sequence_length - current_expected_number + 1
        print(min_removals_needed)

if __name__ == '__main__':
    main()