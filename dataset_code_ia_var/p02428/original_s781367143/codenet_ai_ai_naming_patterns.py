input_size = int(input())
fixed_value, *subset_indices = map(int, input().split())
bit_masks = [1 << idx for idx in range(input_size)]
fixed_mask = 0
for subset_idx in subset_indices:
    fixed_mask |= 1 << subset_idx

for current_mask in range(1 << input_size):
    if (current_mask & fixed_mask) != fixed_mask:
        continue
    present_indices = [mask_idx for mask_idx, bit in enumerate(bit_masks) if current_mask & bit != 0]
    if present_indices:
        print(f'{current_mask}: {" ".join(map(str, present_indices))}')
    else:
        print(f'{current_mask}:')