input_value = int(input())
bit_count = 0
bit_index = 0
while (1 << bit_index) <= input_value:
    if input_value & (1 << bit_index):
        bit_count += 1
    bit_index += 1
print(max(bit_count, bit_index - 1))