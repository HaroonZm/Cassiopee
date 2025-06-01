length, repeat_count = map(int, input().split())
input_string = input()
consecutive_double_o_count = 0
for index in range(len(input_string) - 1):
    if input_string[index] == 'o' and input_string[index + 1] == 'o':
        consecutive_double_o_count += 1
total_consecutive_double_o_count = 0
current_double_o_count = consecutive_double_o_count
for _ in range(repeat_count):
    total_consecutive_double_o_count += current_double_o_count
    current_double_o_count *= 2
output_value = 3 * total_consecutive_double_o_count + length
print(output_value)