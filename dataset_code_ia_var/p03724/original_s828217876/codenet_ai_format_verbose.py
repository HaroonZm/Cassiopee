import sys
from collections import defaultdict

def read_entire_input_as_bytes():
    return sys.stdin.buffer.read()

def read_single_line_as_bytes():
    return sys.stdin.buffer.readline()

def read_single_integer():
    return int(read_single_line_as_bytes())

def read_two_integers():
    return map(int, read_single_line_as_bytes().split())

def read_integer_list_from_line():
    return list(map(int, read_single_line_as_bytes().split()))

def read_integers_from_entire_input():
    return map(int, read_entire_input_as_bytes().split())

def read_single_line_as_string():
    return read_single_line_as_bytes().rstrip().decode('utf-8')

def main():
    number_of_elements, number_of_values_to_be_counted = read_two_integers()

    occurrences_counter = defaultdict(int)

    for value in read_integers_from_entire_input():
        occurrences_counter[value] += 1

    result_string = 'YES'

    for element in range(1, number_of_elements + 1):
        if occurrences_counter[element] % 2 == 1:
            result_string = 'NO'
            break

    print(result_string)

if __name__ == '__main__':
    main()