import re

total_sum = 0
regex_pattern = re.compile(r"\d+")

while True:
    try:
        input_line = input()
        found_numbers = regex_pattern.findall(input_line)
        integer_numbers = [int(number_str) for number_str in found_numbers]
        total_sum += sum(integer_numbers)
    except EOFError:
        break

print(total_sum)