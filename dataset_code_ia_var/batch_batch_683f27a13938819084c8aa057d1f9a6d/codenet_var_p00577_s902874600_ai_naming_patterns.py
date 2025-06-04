input_length = int(input())
input_string = input()

current_index = 0
pattern_count = 0

while current_index + 1 < input_length:
    substring_pair = input_string[current_index:current_index+2]
    if substring_pair in ['OX', 'XO']:
        current_index += 2
        pattern_count += 1
    else:
        current_index += 1

print(pattern_count)