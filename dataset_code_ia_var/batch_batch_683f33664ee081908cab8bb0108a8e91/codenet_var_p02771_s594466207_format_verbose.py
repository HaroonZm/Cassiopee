import sys

read_line_from_stdin = sys.stdin.readline

integer_values_list = list(map(int, read_line_from_stdin().split()))

number_of_unique_values = len(set(integer_values_list))

if number_of_unique_values == 1 or number_of_unique_values == 3:
    print("No")
else:
    print("Yes")