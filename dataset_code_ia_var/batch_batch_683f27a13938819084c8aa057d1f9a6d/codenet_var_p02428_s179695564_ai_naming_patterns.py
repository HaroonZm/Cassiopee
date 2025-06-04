input_bit_count = int(input())
total_combinations = pow(2, input_bit_count)

input_args = list(map(int, input().split()))
active_mask_size = input_args[0]
active_mask_indices = input_args[1:active_mask_size + 1]

def get_active_bits_indices(num, width):
    bin_string = format(num, '0{}b'.format(width))
    return [width - idx - 1 for idx, bit_char in enumerate(bin_string) if bit_char == '1']

if active_mask_size == 0:
    for combo_index in range(total_combinations):
        if combo_index == 0:
            print("0:")
        else:
            active_bits = get_active_bits_indices(combo_index, input_bit_count)
            active_bits_sorted = sorted(active_bits)
            active_bits_str = ' '.join(str(bit_idx) for bit_idx in active_bits_sorted)
            print(f"{combo_index}: {active_bits_str}")
else:
    for combo_index in range(total_combinations):
        if combo_index == 0:
            continue
        active_bits = get_active_bits_indices(combo_index, input_bit_count)
        mask_overlap_count = len(set(active_mask_indices) & set(active_bits))
        if mask_overlap_count == active_mask_size:
            active_bits_sorted = sorted(active_bits)
            active_bits_str = ' '.join(str(bit_idx) for bit_idx in active_bits_sorted)
            print(f"{combo_index}: {active_bits_str}")