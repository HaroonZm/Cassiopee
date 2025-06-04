num_bits = int(input())
_ , *subset_indices_raw = map(int, input().split())
subset_indices_set = set(subset_indices_raw)
for current_value in range(2 ** num_bits):
    if all([(current_value & (1 << subset_index)) for subset_index in subset_indices_set]):
        if current_value == 0:
            print('0:')
        else:
            active_bit_positions = [bit_position for bit_position in range(num_bits) if (current_value & (1 << bit_position))]
            print(f'{current_value}: {" ".join(map(str, active_bit_positions))}')