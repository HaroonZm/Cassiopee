num_bits = int(input())
_, *bit_indices = [int(value) for value in input().split()]

target_mask = 0
for bit_index in bit_indices:
    target_mask |= 1 << bit_index

output_lines = []

for current_value in range(1 << num_bits):
    if (current_value & target_mask) == target_mask:
        output_lines.append(f'{current_value}:')
        for bit_position in range(num_bits):
            if current_value & (1 << bit_position):
                output_lines.append(f' {bit_position}')
        output_lines.append('\n')

print(''.join(output_lines), end='')