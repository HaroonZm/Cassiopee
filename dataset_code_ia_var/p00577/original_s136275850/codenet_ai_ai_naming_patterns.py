input_length = int(input())
input_strings = input().split()
char_list = []
for char in input_strings[0]:
    char_list.append(char)
binary_flags = []
for idx in range(input_length):
    if char_list[idx] == 'O':
        binary_flags.append(1)
    else:
        binary_flags.append(0)
current_index = 0
pair_count = 0
while current_index < input_length - 1:
    if binary_flags[current_index] + binary_flags[current_index + 1] == 1:
        pair_count += 1
        current_index += 2
    else:
        current_index += 1
print(pair_count)