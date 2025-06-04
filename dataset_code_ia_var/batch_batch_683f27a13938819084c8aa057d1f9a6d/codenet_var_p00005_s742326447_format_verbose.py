import sys

def read_integer_list_from_input():
    input_strings = input().split()
    integer_list = []
    for index in range(len(input_strings)):
        integer_list.append(int(input_strings[index]))
    return integer_list

def compute_greatest_common_divisor(first_number, second_number):
    if first_number < second_number:
        return compute_greatest_common_divisor(second_number, first_number)
    if second_number == 0:
        return first_number
    return compute_greatest_common_divisor(second_number, first_number % second_number)

def main():
    input_data_matrix = []
    input_lines = sys.stdin.readlines()

    for input_line in input_lines:
        input_data_matrix.append(input_line.split())

    number_of_input_pairs = len(input_data_matrix)

    for data_row_index in range(number_of_input_pairs):
        first_integer = int(input_data_matrix[data_row_index][0])
        second_integer = int(input_data_matrix[data_row_index][1])

        current_gcd = compute_greatest_common_divisor(first_integer, second_integer)
        current_lcm = (first_integer // current_gcd) * second_integer

        print('%d %d' % (current_gcd, current_lcm))

if __name__ == "__main__":
    main()