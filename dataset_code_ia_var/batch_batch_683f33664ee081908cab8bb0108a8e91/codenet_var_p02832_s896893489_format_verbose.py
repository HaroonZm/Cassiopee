from sys import stdin

number_of_elements = int(stdin.readline().rstrip())

input_sequence = list(map(int, stdin.readline().rstrip().split()))

current_expected_value = 0

for element in input_sequence:
    if element == current_expected_value + 1:
        current_expected_value = element

if current_expected_value == 0:
    print(-1)
else:
    result = number_of_elements - current_expected_value
    print(result)